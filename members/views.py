from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import SignupForm, Profiles 
from .models import Profile


class UserRegistrationForm(CreateView):
    form_class = SignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
# Create your views here.


class UserProfile(UpdateView):
    model = Profile
    form_class : Profiles
    template_name = 'profile.html'

def Profile(request):
    profile = Profile.objects.all()
    return render(request,'base.html', {'profile':profile})