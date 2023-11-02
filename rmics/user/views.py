from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from .forms import LogginForm, CreateUser, ManageUser
from django.http import HttpResponse

# Create your views here.





def create_user(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('ams:add_asset')
    
    else:
        form = CreateUser()
    return render(request, 'user/create-user.html', {'form':form})



def manage_users(request):
    if request.method == "POST":
        form = ManageUser(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('ams:add_asset')
    
    else:
        form = ManageUser()
    return render(request, 'user/manage-users.html', {'form':form})

# def manage_users(request):
#     return render(request, template_name='user/manage-users.html')


def profile(request):
    return render(request, template_name='user/profile.html')