from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.


class BeepManager(models.Manager):
    def rebeep(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        obj = self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
        )
        obj.save()

        return obj


class Beep(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
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
