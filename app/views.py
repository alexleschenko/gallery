from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from app import forms
from app.models import User_Info
from django.views.generic import TemplateView, CreateView, DetailView
# Create your views here.



class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'main.html'

class UserCreate(CreateView):

    model = User
    template_name = 'CreateUser.html'
    form_class = forms.UserCreateForm
    success_url = '/'

class UserProfile(DetailView):
    template_name = 'Profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        current_user = self.request.user
        context['data']=User_Info.objects.filter(user=current_user.id).get()
        return context





