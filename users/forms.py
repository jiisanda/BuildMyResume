from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('email', 'username', )