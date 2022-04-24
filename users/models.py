from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.user.username)

def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)