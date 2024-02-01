from django import forms
from .models import CustomUserProfile, Reward
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group





class UpdateUserForm(UserChangeForm):
# class UpdateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'groups',
            'user_permissions'
        )
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
            'user_permissions': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
        }
        
        exclude = (
            'password1',
            'password2'
        )
        
class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'groups',
            )
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',  'type': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        

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
        
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'plant_assignment': forms.Select(attrs={'class': 'form-control'}),
            'area_assignment': forms.Select(attrs={'class': 'form-control'}),
            'business_unit': forms.Select(attrs={'class': 'form-control'}),
            'motto': forms.TextInput(attrs={'class': 'form-control'}),
        }




class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class AddReward(forms.ModelForm):
    
    class Meta:
        model = Reward
        fields = (
            'title',
            'description',
            'awardee',
            'certificate'
        )
        
        widgets = {
            'awardee': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        