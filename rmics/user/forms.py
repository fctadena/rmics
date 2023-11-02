from django import forms
from .models import CustomUserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


# class CreateUser(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
      
# class CreateUser(forms.ModelForm):
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#     group = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=Group.objects.all())
#     first_name = forms.CharField()
#     last_name = forms.CharField()

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'group', 'last_name', 'first_name']
        
class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'groups')
        

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
        

