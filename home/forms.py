from django import forms

from users.models import NewUser
from .models import Profile, Certificates, Project

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
