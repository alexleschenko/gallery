import os

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.http import request

from app.models import User_Info, Image

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

    def save(self, commit=True):
        user=super(UserCreateForm, self).save(commit=False)
        User_Info.objects.create(user=user.id, country='', date_of_birth='')


class UserInfoUpdate(forms.ModelForm):
    class Meta(object):
        model = User_Info
        exclude = ('id', 'user',)


class AddImage(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('id','url','user',)


