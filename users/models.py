"""
users/models.py

:Models:
```UserManager```
```NewUSer```
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, blank = True)
    phonenumber = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, )
    profile_picture = ResizedImageField(
        size=[300, 300],
        quality=100,
        default="profile_pics/default_profile.png",
        upload_to="profile_pics"
    )
    
    def __str__(self):
        return self.user.email