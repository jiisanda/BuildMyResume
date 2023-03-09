import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from formtools.wizard.views import SessionWizardView

from users.forms import CustomUserChangeForm
from .forms import (ResumeForm, ProfileUpdateFrom, EducationFormSet, ExperienceFormSet, CertificateFormSet,  
                    SkillFormSet, LanguageFormSet, CourseworkFormSet, ChooseForm)
from .models import ResumeMetaData, Experience, Education, Certificate, Skill, Language, Coursework

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FORMS = [
    ('resumes', ResumeForm),
    ('education', EducationFormSet),
    ('experience', ExperienceFormSet),
    ('certificates', CertificateFormSet),
    ('skills', SkillFormSet),
    ('languages', LanguageFormSet), 
    ('courseworks', CourseworkFormSet),
]

FORM_TYPES = ('education', 'experience', 'certificates', 'skills', 'languages', 'courseworks', )

TEMPLATES = {
    'resumes': 'home/resumes.html',
    'education': 'home/education.html',
    'experience': 'home/experience.html',
    'certificates': 'home/certificates.html',
    'skills': 'home/skills.html',
    'languages': 'home/languages.html',
    'courseworks': 'home/courseworks.html',
}


@login_required()
def choose(request, pk):
    user = request.user
    profile_picture_url = user.profile.profile_picture.url.strip('/')
    resume = ResumeMetaData.objects.get(pk=pk)
    form = ChooseForm(request.POST)
    
    if request.method == 'GET':
        form = ChooseForm()
    elif request.method == 'POST' and 'view-resume' in request.POST:
        if form.is_valid() and form.cleaned_data['resume_template'] == 'default':
            return render(request, 'home/default.html', {'form': form, 'resume':resume, 'profile_picture_url':profile_picture_url})
    elif form.is_valid() and request.method == 'POST' and 'export-resume' in request.POST:
        pass
    return render(request, 'home/choose.html', {'form':form, 'resume':resume})


@login_required()
def my_resume(request):
    user = request.user
    resumes = ResumeMetaData.objects.filter(user=user).order_by('-created_at')
    return render(request, 'home/my_resumes.html', {'resumes': resumes})

@login_required()
def templates(request):
    return render(request, 'home/templates.html')

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile has been saved!")
            return HttpResponseRedirect(reverse('home:edit-profile'))
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileUpdateFrom(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'home/profile-edit.html', context)


@login_required()
def delete_my_resume(request, pk):
    resume = ResumeMetaData.objects.get(pk=pk)
    resume.delete()
    messages.success(request, "Resume is successfully deleted!")
    return HttpResponseRedirect(reverse('home:my-resume'))

def dict_has_data(input_dict):
    is_data_present = False
    for key in input_dict:
        if input_dict[key]:
            is_data_present = True
            break
    return is_data_present


class ResumeBucket(LoginRequiredMixin, SessionWizardView):
    login_url = '/login/'
    
    def get_form_initial(self, step):
        if 'pk' in self.kwargs:
            return {}
        return self.initial_dict.get(step, {})
    
    def get_form_instance(self, step):
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            resume = ResumeMetaData.objects.get(id=pk)
            if step == 'resumes':
                return resume
            if step == 'education':
                return resume.education_set.all()
            if step == 'experience':
                return resume.experience_set.all()
            if step == 'certificates':
                return resume.certificate_set.all()
            if step == 'skills':
                return resume.skill_set.all()
            if step == 'languages':
                return resume.language_set.all()
            if step == 'courseworks':
                return resume.coursework_set.all()
        else:
            if step == 'resumes':
                return None
            if step == 'education':
                return Education.objects.none()
            if step == 'experience':
                return Experience.objects.none()
            if step == 'certificates':
                return Certificate.objects.none()
            if step == 'skills':
                return Skill.objects.none()
            if step == 'languages':
                return Language.objects.none()
            if step == 'courseworks':
                return Coursework.objects.none()
        return None
    
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    
    def done(self, form_list, **kwargs):
        user = self.request.user
        resume_form_data = self.get_cleaned_data_for_step('resumes')
        resume_name = resume_form_data['resume_name']
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
        else:
            pk = None
        resume, created = ResumeMetaData.objects.update_or_create(id=pk, defaults={'user':user, 
                                                                                   'resume_name':resume_name, })
        
        for form_name in FORM_TYPES:
            form_data_list = self.get_cleaned_data_for_step(form_name)
            for form_data in form_data_list:
                if not dict_has_data(form_data):
                    continue
                form_data['resume'] = resume
                
                form_instance = self.get_form(step=form_name)
                obj = form_data.pop('id')
                if obj:
                    form_instance.model.objects.filter(id=obj.id).update(**form_data)
                else:
                    form_instance.model.objects.create(**form_data)
        
        messages.add_message(self.request, messages.SUCCESS, message="Resume Saved!")
        return HttpResponseRedirect(reverse('home:my-resume'))
