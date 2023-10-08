"""
users/forms.py

**Forms:**
```SignUpForm```
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .models import User


class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        # validation
        if len(username) < 6:
            raise forms.ValidationError("Username is too short. Make sure your username is at least of length 6")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"{username} is not available... Choose another")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        
        if validate_password(password=password1):
            raise forms.ValidationError("Invalid Password...")
        return password1

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please try again...")
        return super(UserCreationForm, self).clean()
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CustomUserChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # first name fields
        self.fields['first_name'].widget.attrs.update({
            'type': "text",
            'class': "form-control",
            'name': "first_name",
            'maxlength': "30",
            'required': '',
            'id': "id_first_name",
            'placeholder': "First Name*",
        })
        self.fields['last_name'].widget.attrs.update({
            'type': "text",
            'class': "form-control",
            'name': "last_name",
            'maxlength': "30",
            'required': '',
            'id': "id_last_name",
            'placeholder': "Last Name*",
        })
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        }
