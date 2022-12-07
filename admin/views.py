from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import SignupForm, Profiles 
from .models import Profile

''' 
class UserRegistrationForm(CreateView):
    form_class = SignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
# Create your views here. '''

def UserRegistrationForm(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user_profile = Profiles(request.POST, request.FILES)
        
        if form.is_valid() and user_profile.is_valid():
            user = form.save()
            profile = user_profile.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect("login")
    else:
        form = SignupForm()
        user_profile = Profiles()
    
    return render (request, "register.html", {"form":form, "user_profile":user_profile})
    
    
    
    
class UserProfile(UpdateView):
    model = Profile
    form_class : Profiles
    template_name = 'profile.html'

def Profile(request):
    profile = Profile.objects.all()
    return render(request,'base.html', {'profile':profile})