from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, template_name='user/login.html')


def logout(request):
    return render(request, template_name='user/logout.html')


def register_user(request):
    return render(request, template_name='user/register-user.html')



def manage_users(request):
    return render(request, template_name='user/manage-users.html')