from django  import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']fields = ['email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model= Projects
        exclude= ['author', 'created_date', 'author_profile']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']