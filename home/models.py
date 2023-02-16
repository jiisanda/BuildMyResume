"""
home/models.py

:Models: 
```Profile``` ```Social``` ```Education``` ```Certificates``` ```Project```
"""

from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from users.models import NewUser

class Profile(models.Model):
    """Profile
    Stores User Info, related to :model:`users.NewUser`.
    """
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=60, default="")
    lastname = models.CharField(max_length=60, default="")

    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics',
        blank=True,
        default='profile_pics/default_profile.png'
    )
    role = models.CharField(max_length=50, default="")
    phonenumber = models.CharField(max_length=11, default="")

    skills = models.TextField(blank=False, default='')
    coursework = models.TextField(blank=False, default='')

    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user.id) + ' | ' + str(self.user.username)


class Social(models.Model):
    """Social
    Stores Social data of the user, related to :model:`users.NewUser`.
    """
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=64, default="")
    platform_url = models.URLField(max_length=255)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.platform_name)



class Education(models.Model):
    """Education
    Stores Education details of the user, related to :model:`users.NewUser`.
    """
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    school = models.CharField(max_length=200, default="")
    degree = models.CharField(max_length=200, default="")
    startdate = models.DateField(null=True, blank=True, default=None)
    enddate = models.DateField(null=True, blank=True, default=None)
    grade = models.CharField(max_length=10, default="")
    description = models.TextField(max_length=500, default=500)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.school)


class Certificates(models.Model):
    """Certificates
    Stores Certificates details of the user, related to :model:`users.NewUser`.
    """
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=30)
    issued_date = models.DateField(default=timezone.now)
    certificate_id = models.CharField(max_length=200)
    certificate_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.program_name)


class Project(models.Model):
    """Project
    Stores Project details of the user, related to :model:`users.NewUser`.
    """
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    start_duration = models.DateField(default=timezone.now)
    end_duration = models.DateField(default=timezone.now)
    bio_project = models.TextField(blank=True, null=True)
    project_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.project_name)

def create_profile(instance, created, *args, **kwargs):
    """create an instance for every new User"""
    if not created:
        return
    Profile.objects.create(user=instance)
    Social.objects.create(user=instance)
    Education.objects.create(user=instance)
    Certificates.objects.create(user=instance)
    Project.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)

class RecentPost(models.Model):
    '''To be impoted form Blog App'''
