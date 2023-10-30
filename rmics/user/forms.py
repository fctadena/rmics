from django import forms
from .models import CustomUserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        
        

class ManageUser(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('user',
                  'profile_picture',
                  'position',
                  'profession',
                  'plant_assignment',
                  'area_assignment',
                  'business_unit',
                  'motto')
        
        

class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        

