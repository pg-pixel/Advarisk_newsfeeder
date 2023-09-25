"""
This is the views file of App App_user
"""

# import django libraries
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# import custom package
from .forms import CustomRegisterForm


# Create your views here.

class Register(View):
    """
    This class handle view related to registeration of user
    """
    def get(self, request):
        """
        GET request handler for user registration
        """
        registration_form = CustomRegisterForm() 
        
        return render(request, 'register.html', {'registration_form':registration_form}) 
    
    def post(self, request):
        """
        POST request handler for user registration
        """
        registration_form = CustomRegisterForm(request.POST) 
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, ('User added Successfully! Kindly Login to get started...'))
            return redirect('register') 
        
        return render(request, 'register.html', {'registration_form':registration_form})
        
        
        