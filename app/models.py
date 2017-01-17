from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Info(models.Model):
    user = models.ForeignKey(User)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=25)

class Image(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField()

