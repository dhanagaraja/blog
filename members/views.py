from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import SignupForm, Profile


class UserRegistrationForm(CreateView):
    form_class = SignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
# Create your views here.


class UserProfile(UpdateView):
    form_class : Profile
    template_name = 'profile.html'
    success_url = reverse_lazy('index')