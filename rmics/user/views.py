from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LogginForm
from django.http import HttpResponse

# Create your views here.


# def login(request):
#     if request.method == "POST":
#         form = LogginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, username=data['username'], password=data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('ams:asset_list')
            
#             else:
#                 return HttpResponse("Opps! No User Found")
        
#     else:
#         form = LogginForm()
#         return render(request, 'user/login.html', {'form':form})
    



# def logout(request):
#     return render(request, template_name='user/logout.html')


def register_user(request):
    return render(request, template_name='user/register-user.html')



def manage_users(request):
    return render(request, template_name='user/manage-users.html')