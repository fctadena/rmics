from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from .forms import LogginForm, CreateUser, ManageUser, UpdateUserForm
from django.http import HttpResponse
from .models import CustomUserProfile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.db.models import Q







# Create your views here.


def home(request):
    return redirect('login')


def create_user(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            custom_profile = CustomUserProfile.objects.create(user=user)
            messages.success(request, 'CREATED USER SUCCESSFULLY', extra_tags='success')
            return redirect('manage_users')  
            
                 
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
    users = User.objects.select_related('customuserprofile').all()
    
    search_user = request.GET.get('search_user')
    
    if search_user is not None:
        users = users.filter(
            Q(username__icontains=search_user) |
            Q(first_name__icontains=search_user) |
            Q(last_name__icontains=search_user)
        )

    context = {
        'users': users
    }
    return render(request, 'user/user-list.html', context)






    

def manage_users(request):
    user = User.objects.select_related('customuserprofile').all()
    
    search_manage_user = request.GET.get('search_manage_user')
    
    if search_manage_user is not None:
        user = user.filter(
            Q(username__icontains=search_manage_user) |
            Q(first_name__icontains=search_manage_user) |
            Q(last_name__icontains=search_manage_user)
        )

    context = {
        'user':user
    }
    return render(request, 'user/manage-users.html', context)


# def update_user(request, id):
#     user = User.objects.select_related('customuserprofile').get(id=id)
#     user_profile = user.customuserprofile
#     if request.method == "POST":
#         form1 = UpdateUserForm(request.POST, instance=user_profile)
#         if form1.is_valid():
#             user = form1.save()
#             return redirect('profile', id=user.id)
    
#     else:
#         form1 = UpdateUserForm(instance=user)
#         print(user_profile.position)
#     context = {
#         'form1':form1,
#         'user_profile':user_profile
#     }
#     return render(request, 'user/update-user.html', context)
        
def update_user(request, id):
    user = User.objects.select_related('customuserprofile').get(id=id)
    user_profile = user.customuserprofile
    form1 = UpdateUserForm(request.POST, instance=user)
    form2 = ManageUser(request.POST, request.FILES, instance=user_profile)
    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user_profile = form2.save(commit=False)
            user_profile.user = user  # Set the user field of CustomUserProfile
            user_profile.save()
            messages.success(request, 'UPDATED USER SUCCESSFULLY', extra_tags='info')
            return redirect('profile', id=user.id )
        else:
            print(form1.errors)
            print(form2.errors)
        
    else:
        form1 = UpdateUserForm(instance=user)
        form2 = ManageUser(instance=user_profile)
            
    context = {
        'form1':form1,
        'form2':form2,
        'id':id,
        'user':user
    }
    
    return render(request, 'user/update-user.html', context)
    
# def update_user(request, id):
#     user = User.objects.select_related('customuserprofile').get(id=id)
#     current_user = request.user
#     if user == current_user:
#         return redirect('manage_users')
    
#     else:
#         user_profile = user.customuserprofile
#         if request.method == "POST":
#             form1 = UserChangeForm(request.POST, instance=user)
#             form2 = ManageUser(request.POST, request.FILES, instance=user_profile)
#             if form1.is_valid() and form2.is_valid():
#                 user = form1.save()
#                 user_profile = form2.save(commit=False)
#                 user_profile.user = user  # Set the user field of CustomUserProfile
#                 user_profile.save()
#                 return redirect('profile', id=user.id )
        
#         else:
#             form1 = UserChangeForm(instance=user)
#             form2 = ManageUser(instance=user_profile)
            
#         context = {
#             'form1':form1,
#             'form2':form2
#         }
#         return render(request, 'user/update-user.html', context)
    
    
# def update_user(request, id):
#     user = User.objects.select_related('customuserprofile').get(id=id)
#     user_profile = user.customuserprofile
#     if request.method == "POST":
#         form1 = UserChangeForm(request.POST, instance=user)
#         form2 = ManageUser(request.POST, request.FILES, instance=user_profile)
#         if form1.is_valid() and form2.is_valid():
#             user = form1.save()
#             user_profile = form2.save(commit=False)
#             user_profile.user = user  # Set the user field of CustomUserProfile
#             user_profile.save()
#             return redirect('profile', id=user.id )
#         # else:
#         #     print(form1.errors)
#         #     print(form2.errors)
    
#     else:
#         form1 = UserChangeForm(instance=user)
#         form2 = ManageUser(instance=user_profile)
        
#     context = {
#         'form1':form1,
#         'form2':form2
#     }
#     return render(request, 'user/update-user.html', context)


def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        messages.success(request, 'DELETED USER SUCCESSFULLY', extra_tags='warning')
        return redirect('manage_users')
    
    return render(request, 'user/delete-user.html', {'user':user})
        
        
def my_profile(request):
    current_user = User.objects.get(id=request.user.id)
    
    context = {
        'current_user':current_user
    }
    return render(request, 'user/my-profile.html', context)



def settings(request):
    return render(request, 'user/settings.html')