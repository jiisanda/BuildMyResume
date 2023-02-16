"""
users/forms.py

**Forms:**
```SignUpForm```
"""
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
 
class SignUpForm(UserCreationForm):
    """Sign Up Form"""
    class Meta:
        model = NewUser
        fields = ('email', 'username', )