from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from app.models import User_Info

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserInfoUpdate(forms.ModelForm):
    class Meta(object):
        model = User_Info
        exclude = ('id',)