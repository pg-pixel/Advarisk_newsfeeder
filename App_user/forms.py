"""
This is the custom form file for App App_user
"""
# import django libraries
from django import forms 
from django.contrib.auth.forms import UserCreationForm #piggyback
#from django.contrib.auth.models import User #piggyback
from .models import CustomUser

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField() # handling email input 
    
    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password1', 'password2']