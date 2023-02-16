"""
home/admin.py
"""
from django.contrib import admin
from .models import Profile, Social, Education, Certificates, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Education)
admin.site.register(Certificates)
admin.site.register(Project)
