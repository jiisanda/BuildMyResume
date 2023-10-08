"""
users/views.py

"""
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

from .forms import CustomUserCreationForm
from .models import User
from .tokens import account_activation_token


def signup(request):
    """
    Sign Up View
    On-Success: redirect(profile)
    
    **Context:**
    
    **Forms:**
        ```SignUpForm```
    
    **Template:**
    
    :template:`users/signup.html`
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Account | BuildMyResume'
            message = render_to_string('users/account_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_email_to = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[send_email_to])
            email.send()
            messages.success(request, "Verification email sent to {}. Do activate your account".format(user.email))
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "You're now an active subscriber of BuildMyResume! Please login with your valid "
                                  "credentials.")
        return redirect('login')
    else:
        return HttpResponse('Invalid Link!!!')
        
