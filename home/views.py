from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

# from .forms import ProfileForm, UserProfileForm


# Create your views here.
def index(request):
    return render(request, 'home/home.html')

@login_required
def profileTabView(request):
    return render(request, 'home/portfolio.html')

@login_required
def blogTabView(request):
    return render(request, 'home/blog.html')

@login_required
def contactTabView(request):
    return render(request, 'home/contact.html')


# @login_required
# def EditHomePageView(request):
#     if request.method == 'POST':
#         # below two lines will bring all the save data of the user...
#         profile_form = ProfileForm(request.POST, instance=request.user)
#         userprofile_form = UserProfileForm(request.POST, 
#                                             request.FILES, 
#                                             instance=request.user.profile)

#         if profile_form.is_valid() and userprofile_form.is_valid():
#             profile_form.save()
#             userprofile_form.save()
#             messages.success(request, f'Your accout has been updated')
#             return redirect('home:index')
        
#     else:
#         profile_form = ProfileForm(instance=request.user)
#         userprofile_form = UserProfileForm(instance=request.user.profile)
#     context = {
#         'profile_form':profile_form,
#         'userprofile_form':userprofile_form,
#     }

#     return render(request, 'home/edit_home.html', context)
