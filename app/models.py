from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Info(models.Model):
    user = models.ForeignKey(User)
    date_of_birth = models.DateField(blank=True)
    country = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.user



class Image(models.Model):
    user = models.ForeignKey(User, null=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    url = models.CharField(max_length=25, blank=True)


    def __str__(self):
        return self.id

