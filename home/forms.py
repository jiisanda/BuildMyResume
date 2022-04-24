from django.contrib.auth.models import User

from django import forms
from .models import UserProfile, Certificates, Project


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'role', 'coding_lang', 'course_work', 
                'github_url', 'linkedin_url', 'facebook_url', 'instagram_url', 'twitter_url']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = ['program_name', 'platform_name', 'issued_date', 'certificate_id', 
                'certificate_url']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_duration', 'end_duration', 'bio_project', 'project_url']
