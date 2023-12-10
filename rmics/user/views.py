from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from .forms import LogginForm, CreateUser, ManageUser
from django.http import HttpResponse
from .models import CustomUserProfile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




# Create your views here.





def create_user(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:user_list')
    
    else:
        form = CreateUser()
    return render(request, 'user/create-user.html', {'form':form})



    



def profile(request, id):
    user = User.objects.select_related('customuserprofile').get(id=id)
    
    context = {
        'user':user
    }
    
    return render(request, 'user/profile.html', context)
    



def user_list(request):
    user = User.objects.select_related('customuserprofile').all()

    context = {
        'user':user
    }
    return render(request, 'user/user-list.html', context)


    

def manage_users(request):
    user = User.objects.select_related('customuserprofile').all()

    context = {
        'user':user
    }
    return render(request, 'user/manage-users.html', context)

        
def update_user(request, id):
    user = User.objects.select_related('customuserprofile').get(id=id)
    user_profile = user.customuserprofile
    if request.method == "POST":
        form1 = UserChangeForm(request.POST, instance=user)
        form2 = ManageUser(request.POST, request.FILES, instance=user_profile)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user_profile = form2.save(commit=False)
            user_profile.user = user  # Set the user field of CustomUserProfile
            user_profile.save()
            return redirect('user:user_list')
        else:
            print(form1.errors)
            print(form2.errors)
    
    else:
        form1 = UserChangeForm(instance=user)
        form2 = ManageUser(instance=user_profile)
        
    context = {
        'form1':form1,
        'form2':form2
    }
    return render(request, 'user/update-user.html', context)