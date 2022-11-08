from django import forms
from .models import Post

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body',]

        widgets = {
            'title' : forms.TextInput(attrs={"class":"form-control"}),
            'body' : forms.Textarea(attrs={"class":"form-control"})
            
        }