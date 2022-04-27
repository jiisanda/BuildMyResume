from django.contrib.auth.models import User

from django import forms
from .models import UserProfile, Certificates, Project


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-contol', 'placeholder':'First Name*'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name*'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email*'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'role', 'coding_lang', 'course_work', 
                'github_url', 'linkedin_url', 'facebook_url', 'instagram_url', 'twitter_url']

        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Bio...', 'rows':4}),
            'role':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Role...'}),
            'coding_lang':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Coding Languages'}),
            'course_work':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course Work'}),
            'github_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://github.com/username'}),
            'linkedin_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://linkedin.com/username'}),
            'facebook_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://facebook.com/username'}),
            'instagram_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://instagram.com/username'}),
            'twitter_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://twitter.com/username'}),
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = ['program_name', 'platform_name', 'issued_date', 'certificate_id', 
                'certificate_url']
        
        widgets = {
            'program_name':forms.TextInput(attrs={'class':'from-control', 'placeholder':'Program Name*'}),
            'platform_name':forms.TextInput(attrs={'class':'from-control', 'placeholder':'Platform Name*'}),
            'issue_date':forms.DateInput(attrs={'class':'form-control'}),
            'certificate_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Certificate ID'}),
            'certificate_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'Link to drive/site'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_duration', 'end_duration', 'bio_project', 'project_url']

        widgets = {
            'project_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Title*'}),
            'start_duration':forms.DateInput(attrs={'class':'form-class'}),
            'end_duration':forms.DateInput(attrs={'class':'form-control'}),
            'bio_project':forms.Textarea(attrs={'class':'form-control', 'placeholder':'About the project', 'rows':4}),
            'project_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'Link to the Project'}),
        }
