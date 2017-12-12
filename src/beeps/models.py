import re
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from hashtags.signals import parsed_hashtags
from django.db.models.signals import post_save
# Create your models here.


class BeepManager(models.Manager):
    def rebeep(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(user=user, parent=og_parent).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,
        )
        if qs.exists():
            return None

        obj = self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
        )
        obj.save()

        return obj


class Beep(models.Model):
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BeepManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('beep:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']


def beep_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # notify a user
        user_regex = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regex, instance.content)
        # send notification to user here.

        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.content)
        # send hashtag signal to user here.
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)








post_save.connect(beep_save_receiver, sender=Beep)

