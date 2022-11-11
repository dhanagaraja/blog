from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

class UserRegistrationForm(CreateView):
    form_class = SignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
# Create your views here.
