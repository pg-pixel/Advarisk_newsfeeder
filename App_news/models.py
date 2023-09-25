"""
This is the models file of app App_news
"""

# import django libraries
from django.db import models
from django.contrib.auth.models import User # importing django build in User model
from django.conf import settings
# Create your models here.

class SearchHistory(models.Model):
    Manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = None ) # User
    Search_parameter = models.CharField(max_length = 200) # query used to search
    time_stamp = models.DateTimeField(auto_now=True) # last time it is used
    
    def __str__(self):
        return f'{self.Search_parameter}'