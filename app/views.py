from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from app import forms
# Create your views here.
from django.views.generic import TemplateView, CreateView


class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'main.html'

class UserCreate(CreateView):

    model = User
    template_name = 'CreateUser.html'
    form_class = forms.UserCreateForm
    success_url = 'main'