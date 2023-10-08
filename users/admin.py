"""
users/admin.py
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Profile


class UserAdmin(BaseUserAdmin):
    """
    UserAdmin - BaseUserAdmin class 
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', ]
    search_fields = ('email', 'username',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


class ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'phonenumber',
        'address',
        'city',
        'country',
        'linkedin',
        'profile_picture',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
