import os

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.http import request
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView

from app import forms
from app.models import Image, UserDetail


# Create your views here.



class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'



class UserCreate(SuccessMessageMixin, CreateView):
    success_message = 'Thanks for registration'
    model = User
    template_name = 'create_user.html'
    form_class = forms.UserCreateForm
    success_url = '/'




class UserProfile(LoginRequiredMixin, DetailView):
    template_name = 'Profile.html'
    model = User
    context_object_name = 'data'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        current_user = self.request.user
        context['images'] = Image.objects.filter(user=current_user.id)
        return context




class ImagesList(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'images.html'
    context_object_name = 'images'

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserDetail
    template_name = 'user_profile.html'
    form_class = forms.UserInfoUpdate
    success_url = '/'

    def get_object(self):
        return UserDetail.objects.get(user=self.request.user)


class AddImage(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = u'Well Done'
    form_class = forms.AddImage
    template_name = 'upload.html'
    success_url = '/profile/'

    def form_valid(self, form):
        object = form.save(commit=False)
        total_size = object.image.size
        limit = settings.MAX_STORAGE_SIZE
        user_file_total = Image.objects.filter(user=self.request.user.id)
        for i in user_file_total:
            total_size += i.image.size
        if total_size > limit * 1024 * 1024:
            messages.error(self.request, 'Max storage size is {} MB'.format(limit))
            return redirect('/images/add/')
        object.user = self.request.user
        url = os.path.basename(object.image.name)
        url = url.replace(' ', '_')
        object.url = url
        object.save()

        return super(AddImage, self).form_valid(form)


class ImagesListAll(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'images_all.html'
    context_object_name = 'images'
