"""
This is the url routing file of App App_news
"""
# import django libraries
from django.urls import path

# import custom package
from . import views

urlpatterns = [
    path('', views.News.as_view(), name = 'Homepage'),
    path('history/', views.History.as_view(), name = 'History'),
]
