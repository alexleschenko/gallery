from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Info(models.Model):
    user = models.ForeignKey(User)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=25)

    def __str__(self):
        return self.user



class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, null=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    url = models.CharField(max_length=25)


    def __str__(self):
        return self.user.username

