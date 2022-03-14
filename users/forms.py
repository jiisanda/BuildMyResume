from django.contrib.auth.models import User

from django import forms
from users.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), label=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name*'}), label=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name*'}), label=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username*'}), label=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}), label=False)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name*'}), label=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name*'}), label=False)
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username*'}), label=False)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}), label=False)


    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

