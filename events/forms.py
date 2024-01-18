from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import Profile
from .models import Submission
from django import forms

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']
# 
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'name', 'password1', 'password2', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-field--input'}),
            'name':forms.TextInput(attrs={'class':'form-field--input'}),
            'email':forms.EmailInput(attrs={'class':'form-field--input'})
        }