from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput(),
                 'email':forms.EmailInput()}