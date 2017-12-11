from django.db import models
from django.urls import reverse_lazy
# Create your models here.

from beeps.models import Beep

class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): # __unicode__
        return self.tag

    def get_absolute_url(self):
        return reverse_lazy("hashtag", kwargs={"hashtag": self.tag})

    def get_Beeps(self):
        return Beep.objects.filter(content__icontains="#" + self.tag)