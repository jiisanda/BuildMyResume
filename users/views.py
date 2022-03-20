from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import redirect, render

from django.urls import reverse, reverse_lazy

from users.forms import UserForm,  EditUserForm
from users.models import Profile

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponse("ACCOUNT ACTIVE")
                return HttpResponseRedirect(reverse('home:index')) 
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to logon and failed...")
            print(f"User: {username} and password {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'users/login.html', {})


def registrationView(request):
    registered = False
    # if this is the POST request we need to process the form data
    if request.method == "POST":
        # creating a form instance and populate it with data from the request: 
        user_form = UserForm(request.POST)
        # checking the form is valid
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'users/registration.html',
                            {'user_form':user_form,
                            'registered':registered})


@login_required
def edit_profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:login')
            # return redirect(to='chats_app:home')
    else:
        user_form = EditUserForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {
        'user_form':user_form,
    })

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = 'Successfully Changed Your Password'
    success_url = reverse_lazy('users:login')