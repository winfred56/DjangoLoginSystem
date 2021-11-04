from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm

class SignupForms(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
