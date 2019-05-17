from django import forms
from django.forms.models import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['types','headline','content']
        # widgets={'content':forms.TextInput()}
               


        