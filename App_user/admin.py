from django.contrib import admin

# Register your models here.
from .models import CustomUser 

def allow_user(modeladmin, request, queryset):
    queryset.update(is_blocked = False, daily_request_limit=10)  # Set the daily request limit as needed 
    
def block_user(modeladmin, request, queryset):
    queryset.update(is_blocked = True) 
    
allow_user.short_description = "Allow selected users"
block_user.short_description = "Block selected users" 

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_blocked', 'daily_request_limit')
    actions = [allow_user, block_user]
    
admin.site.register(CustomUser, CustomUserAdmin)








