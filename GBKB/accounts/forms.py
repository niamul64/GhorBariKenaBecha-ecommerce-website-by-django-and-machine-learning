from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User    # default user model importing
from .models import ExtentionUser   # importing ExtentionUser model from models.py


class UserReg(UserCreationForm):   # user model form formating for frontend

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )


class ExtentUser(forms.ModelForm):  # ExtentionUser model form formating for frontend

    class Meta:
        model = ExtentionUser
        fields = ('mobileNumber',)