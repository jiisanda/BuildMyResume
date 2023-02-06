from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from .forms import HomeProfileForm, UserProfileForm


# Create your views here.
def index(request):
    return render(request, 'home/home.html')

@login_required
def profile_tab_view(request):
    return render(request, 'home/portfolio.html')

@login_required
def blog_tab_view(request):
    return render(request, 'home/blog.html')

@login_required
def contact_tab_view(request):
    return render(request, 'home/contact.html')


@login_required
def edit_home_page_view(request):
    if request.method == 'POST':
        # below two lines will bring all the save data of the user...
        home_profile_form = HomeProfileForm(request.POST, request.FILES, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, 
                                            request.FILES, 
                                            instance=request.user.profile)

        if home_profile_form.is_valid() and user_profile_form.is_valid():
            home_profile_form.save()
            user_profile_form.save()
            messages.success(request, f'Your accout has been updated')
            return redirect('home:index')
        
    else:
        home_profile_form = HomeProfileForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)
    context = {
        'home_profile_form':home_profile_form,
        'user_profile_form':user_profile_form,
    }

    return render(request, 'home/edit_home.html', context)
