import os

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.http import request

from app.models import User_Info, Image

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserInfoUpdate(forms.ModelForm):
    class Meta(object):
        model = User_Info
        exclude = ('id',)


class AddImage(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('id','url','user',)


