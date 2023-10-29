from django.urls import path
from .models import UserProfile
from . import views


#####-WIP
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register-user/', views.register_user, name='register_user'),
    path('manage-users/', views.manage_users, name='manage_users'),
]
