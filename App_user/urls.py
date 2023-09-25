"""
This is the url routing file of App App_user.
We are piggybacking on django provided views for logging and logout
"""
# import django libraries
from django.urls import path 
from django.contrib.auth import views as auth_views

# import custom package
from App_user import views

urlpatterns = [
    path('', views.Register.as_view() , name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'), #piggybacking
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html') , name = 'logout'), #piggybacking

]
