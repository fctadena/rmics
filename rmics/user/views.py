from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from .forms import LogginForm, CreateUser, ManageUser, UpdateUserForm, AddReward
from django.http import HttpResponse
from .models import CustomUserProfile, Reward
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.db.models import Q
from .decorators import unauthenticated_logic, allowed_groups





def home(request):
    return redirect('login')

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super'])
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








@unauthenticated_logic
def profile(request, id):
    user = User.objects.select_related('customuserprofile').get(id=id)
    user_rewards = Reward.objects.filter(awardee=user)

    
    context = {
        'user':user,
        'user_rewards':user_rewards
    }
    
    return render(request, 'user/profile.html', context)
    


@unauthenticated_logic
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






    
@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst', 'National Management'])
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




@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'National Management'])     
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
    

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'National Management'])
def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        messages.success(request, 'DELETED USER SUCCESSFULLY', extra_tags='warning')
        return redirect('manage_users')
    
    return render(request, 'user/delete-user.html', {'user':user})
        
@unauthenticated_logic        
def my_profile(request):
    current_user = User.objects.get(id=request.user.id)
    
    context = {
        'current_user':current_user
    }
    return render(request, 'user/my-profile.html', context)


@unauthenticated_logic
def settings(request):
    return render(request, 'user/settings.html')



@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def add_reward(request, id):
    awardee = get_object_or_404(User, id=id)
    award_form = AddReward(initial={'awardee': awardee})
    
    if request.method == "POST":
        data = AddReward(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'ADDED AWARD SUCCESSFULLY', extra_tags='success')
            return redirect('profile', id=awardee.id)
        else:
            print("FORM NOT VALID:", data.errors)

    context = {
        "award_form": award_form,
        "awardee": awardee,
    }

    return render(request, template_name='user/add-reward.html', context=context)



@unauthenticated_logic
def rewards_summary(request):
    rewards = Reward.objects.all()
    
    context = {
        'rewards': rewards
    }
    
    return render(request, template_name='user/rewards-summary.html', context=context)

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def delete_reward(request, id):
    reward = Reward.objects.get(id=id)
    
    if request.method == "POST":
        reward.delete()
        messages.success(request, 'REWARD DELETED SUCCESSFULLY', extra_tags='warning')
        return redirect('rewards_summary')
        
    context = {
        'reward':reward,
    }
    
    return render(request, template_name='user/delete-reward.html', context=context)

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def edit_reward(request, id):
    reward = Reward.objects.get(id=id)
    reward_form = AddReward(instance=reward)
    
    if request.method == "POST":
        reward_form = AddReward(request.POST, request.FILES, instance=reward)
        if reward_form.is_valid():
            reward_form.save()
            messages.success(request, 'REWARD UPDATED SUCCESSFULLY', extra_tags='info')
            return redirect('reward_detail', id=id)
        else:
            messages.error(request, 'Please correct the errors below.', extra_tags='danger')
    
    else:
        reward_form = AddReward(instance=reward)
        awardee = reward.awardee
        
    context = {
        'reward_form':reward_form,
        'awardee':awardee
    }    
    
    
    return render(request, template_name='user/edit-reward.html', context=context)


@unauthenticated_logic
def reward_detail(request, id):
    reward = Reward.objects.get(id=id)
    
    context = {
        'reward':reward,
    }

    return render(request, template_name='user/reward-detail.html', context=context)

