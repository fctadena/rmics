from django.urls import path
from .models import CustomUserProfile
from . import views
from django.contrib.auth import views as authentication_views


#####-WIP
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html', next_page='drms:maintenance_records', redirect_authenticated_user=True), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('change-password/', authentication_views.PasswordChangeView.as_view(template_name='user/change-password.html', success_url='/success-password-change/')),
    path('success-password-change/', authentication_views.PasswordChangeDoneView.as_view(template_name='user/password-change-success.html')),
    path('create-user/', views.create_user, name='create_user'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('user-list/', views.user_list, name='user_list'),
    path('update-user/<int:id>/', views.update_user, name='update_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('my-profile', views.my_profile, name='my_profile'),


]
