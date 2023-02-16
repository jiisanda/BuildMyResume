"""
home/views.py
Contains: 
index view, edit_home_page_view, profile_tab_view, blog_tab_view
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from users.models import NewUser

from .forms import HomeProfileForm, UserProfileForm
from .models import Profile


# Create your views here.
@login_required
def index(request, username: str):
    """
    Displaying the home page, login required to view home page of the user.

    **Context:**
    ``NewUser``
        An instance of :NewUser:`users.NewUser`.
        
    **Template:**
    
    :template:`home/home.html`.
    """
    context = {}
    try:
        uname = NewUser.objects.get(username=username)
    except NewUser.DoesNotExist:
        uname = None
    context['user'] = uname
    return render(request, 'home/home.html', context)

@login_required
def profile_tab_view(request):
    """
    Profile tab of the user, login required.
    
    **Context:**
    
    **Template:**
    
    :template:`home/protfolio.html`.
    """
    return render(request, 'home/portfolio.html')

@login_required
def blog_tab_view(request):
    """
    Blog Tab, login is required.
    
    **Context:**
    
    **Template:**
    
    :template:`home/blog.html`.
    """
    return render(request, 'home/blog.html')

@login_required
def contact_tab_view(request):
    """
    Contact form, login is required.
    
    **Context:**
    
    **Template:**
    
    :template:`home/contact.html`.
    """
    return render(request, 'home/contact.html')


@login_required
def edit_home_page_view(request, username: str):
    """
    Edit Home Page, login is required.
    
    **Context:**
    ``NewUser``
        An instance of :NewUser:`users.NewUser`.
    ``Profile``
        An instance of :Profile:`home:Profile`.
    
    **Forms:**
    ```HomeProfileForm```
    ```UserProfileForm```
    
    **Template:**
    
    :template:`home/edit_home.html`
    """
    requested_user = NewUser.objects.get(username=username)
    requested_user_profile = Profile.objects.get(id=requested_user.id)
    if request.method == 'POST':
        # below two lines will bring all the save data of the user...
        # request_user = get_object_or_404(Profile, id=id)
        home_profile_form = HomeProfileForm(request.POST,
                                            request.FILES,
                                            instance=requested_user
                                        )
        user_profile_form = UserProfileForm(request.POST,
                                            instance=request.user.profile
                                        )

        if home_profile_form.is_valid() and user_profile_form.is_valid():
            home_profile_form.save()
            user_profile_form.save()
            success_msg = 'Your accout has been updated'
            messages.success(request, success_msg)
            return redirect('home:index', username=username)

    else:
        home_profile_form = HomeProfileForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)
    context = {
        'home_profile_form':home_profile_form,
        'user_profile_form':user_profile_form,
        'requested_user':requested_user,
        'requested_user_profile':requested_user_profile,
    }

    return render(request, 'home/edit_home.html', context)
