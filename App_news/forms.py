"""
This is the forms file of App App_news
"""

# import django libraries
from django import forms 

# import custom package
from App_news.models import SearchHistory # importing model

class SearchHistoryForm(forms.ModelForm): # using model form
    class Meta:
        model = SearchHistory
        fields = ['Search_parameter']
