from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('my-profile/', views.profileTabView, name='profile'),
    path('my-blog/', views.blogTabView, name='blog'),
    path('contact-me/', views.contactTabView, name='contact'),
]
