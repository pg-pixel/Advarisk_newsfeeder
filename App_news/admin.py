
from django.contrib import admin
from . models import SearchHistory 
# Register your models here.

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('Manager','Search_parameter','time_stamp')  
    ordering = ('-time_stamp',) # order by timestamp