"""
home/urls.py

URLs for app_name: home
"""

from django.urls import path

from . import views
from users import views as user_views

app_name = 'home'

urlpatterns = [
    path('my-resume', views.my_resume, name='my-resume'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('delete/<int:pk>.', views.delete_my_resume, name='delete-resume'),
    path('resume/create/', views.ResumeBucket.as_view(views.FORMS), name='create-resume'),
    path('edit/resume/<int:pk>/', views.ResumeBucket.as_view(views.FORMS), name='edit-resume'),
    path('templates/', views.templates, name='templates'),
    path('resume/<int:pk>/choose-template/', views.choose, name='choose'),
    path('resume/<int:pk>/view-resume/', views.choose, name='views-resume'),
]
