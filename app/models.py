from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = settings.MAX_UPLOAD_SIZE
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

# Create your models here.

class Image(models.Model):


    user = models.ForeignKey(User, null=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, validators=[validate_image])
    url = models.CharField(max_length=25, blank=True)


class UserDetail(models.Model):
    country=models.CharField(max_length=100)
    user=models.OneToOneField(User)