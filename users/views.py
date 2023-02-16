"""
users/views.py

:contains:
```UserView```
```signup```
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import SignUpForm


class UserView(DetailView):
    """
    **Context:**
        
    **Template:**
    
    :redirect-template:`home/home.html`.
    """
    template_name = 'home/home.html'

    def get_object(self, querset=None):
        if querset is None:
            querset = self.get_queryset()
        return self.request.user

def signup(request):
    """
    Sign Up View
    On-Success: redirect(users:profile)
    
    **Context:**
    
    **Forms:**
        ```SignUpForm```
    
    **Template:**
    
    :template:`users/signup.html`
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
