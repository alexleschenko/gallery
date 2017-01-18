from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Image


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", 'email')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        user.save()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user



class AddImage(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('id', 'url', 'user',)
