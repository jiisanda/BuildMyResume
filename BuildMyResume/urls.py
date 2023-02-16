"""BuildMyResume URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls')),
    path('', include('home.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
