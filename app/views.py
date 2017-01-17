import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from app import forms
from app.models import User_Info, Image
from django.views.generic import TemplateView, CreateView, DetailView, ListView
# Create your views here.



class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'main.html'

class UserCreate(CreateView):

    model = User
    template_name = 'CreateUser.html'
    form_class = forms.UserCreateForm
    success_url = '/'

class UserProfile(LoginRequiredMixin,DetailView):
    template_name = 'Profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        current_user = self.request.user
        context['data']=User_Info.objects.filter(user=current_user.id).get()
        return context

class ImagesList(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'Image_List.html'
    context_object_name = 'images'


class AddImage(LoginRequiredMixin, CreateView):
    form_class = forms.AddImage
    template_name = 'upload.html'
    success_url = '/images/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        url = os.path.basename(object.image.name)
        object.url = url
        object.save()
        return super(AddImage, self).form_valid(form)




