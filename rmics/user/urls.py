from django.urls import path
from .models import UserProfile
from . import views
from django.contrib.auth import views as authentication_views


#####-WIP
urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html', next_page='ams:add_asset', redirect_authenticated_user=True), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('change-password/', authentication_views.PasswordChangeView.as_view(template_name='user/change-password.html', success_url='/success-password-change/')),
    path('success-password-change/', authentication_views.PasswordChangeDoneView.as_view(template_name='user/password-change-success.html')),
    path('register-user/', views.register_user, name='register_user'),
    path('manage-users/', views.manage_users, name='manage_users'),
]
