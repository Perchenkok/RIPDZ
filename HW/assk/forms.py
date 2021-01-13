from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from assk.models import *

class NewPost(forms.ModelForm):
    tags = forms.CharField(required= False)

    class Meta:
        model = Post
        fields = ['title', 'text']

class NewAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'text']