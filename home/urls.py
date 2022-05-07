from django.urls import path

from .views import index, profileTabView, blogTabView, contactTabView    #, EditHomePageView

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('my-profile/', profileTabView, name='profile'),
    path('my-blog/', blogTabView, name='blog'),
    path('contact-me/', contactTabView, name='contact'),
    # path('edit-home-page/', EditHomePageView, name="edit_home")
]
