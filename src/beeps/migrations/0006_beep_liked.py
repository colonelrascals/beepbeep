# Generated by Django 2.0 on 2017-12-12 18:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beeps', '0005_beep_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='beep',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
