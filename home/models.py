from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50, )

    def __str__(self):
        return str(self.role_name)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})


class CodingLang(models.Model):
    coding_lang = models.CharField(max_length=20, )

    def __str__(self):
        return str(self.coding_lang)


class CourseWork(models.Model):
    coursework = models.CharField(max_length=30)

    def __str__(self):
        return str(self.coursework)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True, default='profile_pics/default_profile.png')
    role = models.CharField(max_length=50, default="Student")
    coding_lang = models.CharField(max_length=20)
    course_work = models.CharField(max_length=30)
    github_url = models.URLField(max_length=200)
    linkedin_url = models.URLField(max_length=200)
    facebook_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    twitter_url = models.URLField(max_length=200)
    last_modeified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.email)


class PlatformName(models.Model):
    paltform_name = models.CharField(max_length=30)
    platform_url = models.URLField(max_length=200)
    platform_logo = models.ImageField(upload_to='platform_logo', default='home/default-platform.png')

    def __str__(self):
        return str(self.paltform_name)

class Certificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=30)
    issuerd_date = models.DateField(auto_now=True)
    certificate_id = models.CharField(max_length=200)
    certificate_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.username) + ' | ' + str(self.program_name)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    start_duration = models.DateField(auto_now=True)
    end_duration = models.DateField(auto_now=True)
    bio_project = models.TextField(blank=True, null=True)
    project_url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.username) + ' | ' + str(self.project_name)


class RecentPost(models.Model):
    '''To be impoted form Blog App'''
    pass

