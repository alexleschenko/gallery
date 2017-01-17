from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView


class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'main.html'
