"""
home/forms.py

**Forms:**
    ```HomeProfileForm```
    ```UserProfileForm```
    ```CertificateForm```
    ```ProjectForm```
"""

from django import forms
from django.conf import settings

from users.models import Profile
from .models import ResumeMetaData, Experience, Certificate, Education, Skill, Language, Coursework, Project
from .choices import RESUME_CHOICES


class ProfileUpdateFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # position field
        self.fields['position'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"position",
            'maxlength':"30",
            'required':'',
            'id':"id_position",
            'placeholder':"Position*",
        })
        # address field
        self.fields['address'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"address",
            'maxlength':"30",
            'required':'',
            'id':"id_address",
            'placeholder':"Address*",
        })
        # city field
        self.fields['city'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"city",
            'maxlength':"30",
            'required':'',
            'id':"id_city",
            'placeholder':"City*",
        })
        # country field
        self.fields['country'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"country",
            'maxlength':"30",
            'required':'',
            'id':"id_countryn",
            'placeholder':"Country*",
        })
        # phonenumber field
        self.fields['phonenumber'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"phonenumber",
            'maxlength':"30",
            'required':'',
            'id':"id_phonenumber",
            'placeholder':"Mobile Number*",
        })
        # linkedin
        self.fields['linkedin'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"linkedin",
            'maxlength':'1024',
            'required':'',
            'id':"id_linkedin",
            'placeholder':"LinkedIn",
        })
        # github
        self.fields['github'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"github",
            'maxlength':'1024',
            'required':'',
            'id':"id_github",
            'placeholder':"Github",
        })
        # bio field
        self.fields['bio'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"bio",
            'maxlength':'1024',
            'required':'',
            'id':"id_bio",
            'placeholder':"Bio",
        })
        # profile_picture field
        self.fields['profile_picture'].widget.attrs.update({
            'type':'file',
            'class':'form-control',
            'name':'profile_picture',
            'accept':'image/',
            'id':'id_profile_picture',
        })
    
    class Meta:
        model = Profile
        fields = ['position', 'address', 'city', 'country', 'phonenumber', 'linkedin', 'github', 'bio', 'profile_picture']
        widgets = {
            'position': forms.TextInput(attrs={'placeholder':'Job Title/Role'}),
            'address': forms.TextInput(attrs={'placeholder':'Address'}),
            'city': forms.TextInput(attrs={'placeholder':'City'}),
            'country': forms.TextInput(attrs={'placeholder':'Country'}),
            'phonenumber': forms.TextInput(attrs={'placeholder':'Mobile Number'}),
            'linkedin': forms.URLInput(attrs={'placeholder':'LinkedIn Profile'}),
            'github': forms.URLInput(attrs={'placeholder':'GitHub Profile'}),
            'bio': forms.Textarea(attrs={'cols':5}),
        }
        labels = {
            "linkedin": "LinkedIn Profile",
            "github": "GitHub Profile",
            "phonenumber": "Mobile Number",
            "profile_picture": "Profile Picture",
            "bio": "Bio",
        }


class ChooseForm(forms.Form):
    resume_template = forms.ChoiceField(choices=RESUME_CHOICES, required=True)
    
    class Meta:
        pass


class MyModelFormSet(forms.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(MyModelFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = ResumeMetaData
        fields = ['resume_name', 'user', 'id', ]
        widgets = {
            'resume_name': forms.TextInput(attrs={'placeholder':'Ex.: Backend Developer'}),
            'user': forms.HiddenInput(),
            'id': forms.HiddenInput(),
        }
        labels = {
            'resume_name':'Resume Name',
        }


class ExperienceForm(forms.ModelForm):
    start_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                    'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    end_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                   'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    
    class Meta:
        model = Experience
        fields = ['position', 'company', 'city', 'start_date', 'end_date', 'description', 'resume', ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'objective-box', 'cols':50, 'rows':10}),
            'position': forms.TextInput(attrs={'placeholder':'Ex.: Backend Developer'}),
            'company': forms.TextInput(attrs={'placeholder':'Company Name'}),
            'city': forms.TextInput(attrs={'placeholder':'Location'}),
            'resume':forms.HiddenInput()
        }

ExperienceFormSet = forms.modelformset_factory(Experience, form=ExperienceForm, formset=MyModelFormSet, extra=1, max_num=5)


class EducationForm(forms.ModelForm):
    start_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                    'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    end_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                    'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    
    class Meta:
        model = Education
        fields = ['school', 'degree', 'major', 'grade', 'start_date', 'end_date', 'resume', ]
        widgets = {
            'school': forms.TextInput(attrs={'placeholder':'School Name'}),
            'degree': forms.TextInput(attrs={'placeholder':'Degree'}),
            'major': forms.TextInput(attrs={'placeholder':'Major'}),
            'grade': forms.NumberInput(attrs={'placeholder':'Grade'}),
            'resume': forms.HiddenInput(),
        }
        labels = {
            'grade':'Grade'
        }


EducationFormSet = forms.modelformset_factory(Education, form=EducationForm, formset=MyModelFormSet, max_num=3)


class CertificateForm(forms.ModelForm):
    issued_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                     'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                 }))

    class Meta:
        model = Certificate
        fields = ['program_name', 'issued_date', 'platform_name', 'certificate_id', 'certificate_url', 'resume', ]
        widgets = {
            'program_name': forms.TextInput(attrs={'placeholder':'Program Name'}),
            'platform_name': forms.TextInput(attrs={'placeholder':'Platform Name'}),
            'certificate_id': forms.TextInput(attrs={'placeholder':'Certificate ID'}),
            'certificate_url': forms.URLInput(attrs={'placeholder':'Certificate URL'}),
            'resume': forms.HiddenInput(),
        }
        labels = {
            'program_name':'Program Name',
        }

CertificateFormSet = forms.modelformset_factory(Certificate, form=CertificateForm, formset=MyModelFormSet, max_num=5)


class SkillForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(SkillForm, self).clean()
        skill_name = cleaned_data.get('skill_name')
        proficiency = cleaned_data.get('proficiency')
        
        if skill_name and proficiency not in [1, 2, 3, 4, 5]:
            raise forms.ValidationError("Please select a proficiency level for skills...")
        
        if proficiency in [1, 2, 3, 4, 5] and not skill_name:
            raise forms.ValidationError("Please enter a skill...")
    
    class Meta:
        model = Skill
        fields = ['skill_name', 'proficiency', 'resume', ]
        widgets = {
            'proficiency': forms.Select(attrs={'class':'form-control'}),
            'skill_name': forms.TextInput(attrs={'placeholder':'Ex.: Python'}),
            'resume': forms.HiddenInput(),
        }
        label={
            'skill_name': 'Skill Name',
        }

SkillFormSet = forms.modelformset_factory(Skill, form=SkillForm, formset=MyModelFormSet, max_num=5)


class LanguageForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(LanguageForm, self).clean()
        language_name = cleaned_data.get('language_name')
        proficiency = cleaned_data.get('proficiency')
        
        if language_name and proficiency not in [1, 2, 3, 4, 5]:
            raise forms.ValidationError("Please select a proficiency level for language...")
        
        if proficiency in [1, 2, 3, 4, 5] and not language_name:
            raise forms.ValidationError("Please enter a language...")
    
    class Meta:
        model = Language
        fields = ['language_name', 'proficiency', 'resume', ]
        widgets = {
            'proficiency': forms.Select(attrs={'class':'form-control'}),
            'language_name': forms.TextInput(attrs={'placeholder':'Language Ex.: Japanese'}),
            'resume': forms.HiddenInput(),
        }
        label={
            'language_name': 'Language Name',
        }

LanguageFormSet = forms.modelformset_factory(Language, form=LanguageForm, formset=MyModelFormSet, max_num=5)


class CourseworkForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CourseworkForm, self).clean()
        coursework_name = cleaned_data.get('coursework_name')
        proficiency = cleaned_data.get('proficiency')
        
        if coursework_name and proficiency not in [1, 2, 3, 4, 5]:
            raise forms.ValidationError("Please select a proficiency level for coursework...")
        
        if proficiency in [1, 2, 3, 4, 5] and not coursework_name:
            raise forms.ValidationError("Please enter a coursework...")
    
    class Meta:
        model = Coursework
        fields = ['coursework_name', 'proficiency', 'resume', ]
        widgets = {
            'proficiency': forms.Select(attrs={'class':'form-control'}),
            'coursework_name': forms.TextInput(attrs={'placeholder':'Ex.: Database Management'}),
            'resume': forms.HiddenInput(),
        }
        label={
            'coursework_name': 'Coursework Name',
        }

CourseworkFormSet = forms.modelformset_factory(Coursework, form=CourseworkForm, formset=MyModelFormSet, max_num=5)


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                    'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    end_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={
                                    'class':'date-picker', 'placeholder':'DD/MM/YYYY',
                                }))
    
    class Meta:
        model = Project
        fields= ['project_name', 'stack_name', 'project_link', 'start_date', 'end_date', 'description', 'resume', ]
        widgets = {
            'project_name': forms.TextInput(attrs={'placeholder':'Project Name'}),
            'stack_name': forms.TextInput(attrs={'placeholder':'Stack Name'}),
            'project_link': forms.URLInput(attrs={'placeholder':'Project Link'}),
            'description': forms.Textarea(attrs={'class':'objective-box', 'cols':50, 'rows':10}),
            'resume': forms.HiddenInput(),
        }
        label = {
            'project_name': 'Project Name',
        }

ProjectFormSet = forms.modelformset_factory(Project, form=ProjectForm, formset=MyModelFormSet, max_num=5)
