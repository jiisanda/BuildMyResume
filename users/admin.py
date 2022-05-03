from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', )
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('id', 'email', 'username', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields':('email', 'username', )}),
        ('Permissions', {'fields':('is_staff', 'is_active', )}),
        # ('Personal', {'fields':()}),
    )

    # formfield_override = {
    #     NewUser.about: {'widget':Textarea(attrs={'rows':10, 'cols':40})},
    # }

    add_fieldsets = (
        (None, {
            'classes':('wide', ),
            'fields':('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(NewUser, UserAdminConfig)