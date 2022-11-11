from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", }),label="Email ")
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control",}), label="First Name ")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control",}), label="Last Name ")
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control", }), label="Username ")
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control", }), label="Password ")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control",}), label="Re-Type Password ")
   
    class Meta:
        model=User
        fields= ('username','first_name','last_name','email', 'password1','password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
    
#    def __init__(self,*args, **kwargs):
#        super(SignupForm, self).__init__(*args,**kwargs)
#        self.fields['username'].widget.attrs['class'] = 'form-control'
#        self.fields['password1'].widget.attrs['class'] = 'form-control'
#        self.fields['password2'].widget.attrs['class'] = 'form-control'
class LoginForm(AuthenticationForm):
    def __init__ (self, *args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        
    username =UsernameField(widget=forms.TextInput(attrs={'class':"form-control"}))
    username =forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))