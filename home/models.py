from django.db import models

from .choices import LANGUAGE_PROFICIENCY_CHOICES, SKILL_PROFICIENCY_CHOICES, COURSEWORK_PROFICIENCY_CHOICES
from users.models import User


class ResumeMetaData(models.Model):
    resume_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f"{self.resume_name} | {self.user.username}"


class Experience(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    position = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-end_date', ]


class Education(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    school = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    university = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    grade = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.school
    
    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-end_date', ]


class Certificate(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    program_name = models.CharField(max_length=255, blank=True)
    platform_name = models.CharField(max_length=255, blank=True)
    issued_date = models.DateField(blank=True, null=True)
    certificate_id = models.CharField(max_length=255, blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.platform_name

    class Meta:
        ordering = ['-issued_date', ]


class Skill(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    skill_name = models.CharField(max_length=255, blank=True)
    proficiency = models.IntegerField(choices=SKILL_PROFICIENCY_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.skill_name


class Language(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    language_name = models.CharField(max_length=255, blank=True)
    proficiency = models.IntegerField(choices=LANGUAGE_PROFICIENCY_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.language_name


class Coursework(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    coursework_name = models.CharField(max_length=255, blank=True)
    proficiency = models.IntegerField(choices=COURSEWORK_PROFICIENCY_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.coursework_name


class Project(models.Model):
    resume = models.ForeignKey(ResumeMetaData, on_delete=models.CASCADE, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    stack_name = models.CharField(max_length=255, blank=True)
    project_link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.project_name
