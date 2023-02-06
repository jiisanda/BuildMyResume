from django.urls import path

from .views import index, profile_tab_view, blog_tab_view, contact_tab_view, edit_home_page_view

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('my-profile/', profile_tab_view, name='profile'),
    path('my-blog/', blog_tab_view, name='blog'),
    path('contact-me/', contact_tab_view, name='contact'),
    path('edit-home-page/', edit_home_page_view, name="edit_home")
]
