from django.db import models
from django.db.models.signals import post_save

from users.models import NewUser

from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=60, default="")
    lastname = models.CharField(max_length=60, default="")

    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True, default='profile_pics/default_profile.png')
    role = models.CharField(max_length=50, default="")
    phonenumber = models.CharField(max_length=11, default="")

    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user.id) + ' | ' + str(self.user.username)


def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)


class Social(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=64, default="")
    platform_url = models.URLField(max_length=255)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.platform_name)

def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Social.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)


class Education(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    school = models.CharField(max_length=200, default="")
    degree = models.CharField(max_length=200, default="")
    startdate = models.DateField(null=True, blank=True, default=None)
    enddate = models.DateField(null=True, blank=True, default=None)
    grade = models.CharField(max_length=10, default="")
    description = models.TextField(max_length=500, default=500)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.school)
    
def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Education.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)


class Skill(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    coding_lang = models.CharField(max_length=20, default="")
    coursework = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.user.username)

def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Skill.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)


class CodingLang(models.Model):
    coding_lang = models.CharField(max_length=20, )

    def __str__(self):
        return str(self.coding_lang)


class CourseWork(models.Model):
    coursework = models.CharField(max_length=30)

    def __str__(self):
        return str(self.coursework)


class PlatformName(models.Model):
    paltform_name = models.CharField(max_length=30)
    platform_url = models.URLField(max_length=200)
    platform_logo = models.ImageField(upload_to='platform_logo', default='home/default-platform.png')

    def __str__(self):
        return str(self.paltform_name)

class Certificates(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=30)
    issued_date = models.DateField(default=timezone.now)
    certificate_id = models.CharField(max_length=200)
    certificate_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.program_name)


def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Certificates.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)


class Project(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    start_duration = models.DateField(default=timezone.now)
    end_duration = models.DateField(default=timezone.now)
    bio_project = models.TextField(blank=True, null=True)
    project_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.user.username) + ' | ' + str(self.project_name)

def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return 
    Project.objects.create(user=instance)
post_save.connect(create_profile, sender=NewUser)

class RecentPost(models.Model):
    '''To be impoted form Blog App'''
    pass

