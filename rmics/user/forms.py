from django import forms
from .models import CustomUserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class UpdateUserForm(UserCreationForm):
    # position = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'groups')
        

class ManageUser(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = (
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
        

