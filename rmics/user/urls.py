from django.urls import path, include
from .models import CustomUserProfile
from . import views
from django.contrib.auth import views as authentication_views


#####-WIP
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html', next_page='drms:maintenance_records', redirect_authenticated_user=True), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('change-password/', authentication_views.PasswordChangeView.as_view(template_name='user/change-password.html', success_url='/success-password-change/'), name='change_password'),
    path('success-password-change/', authentication_views.PasswordChangeDoneView.as_view(template_name='user/password-change-success.html')),
    path('settings/', views.settings, name='settings'),
    path('create-user/', views.create_user, name='create_user'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('user-list/', views.user_list, name='user_list'),
    path('update-user/<int:id>/', views.update_user, name='update_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('my-profile', views.my_profile, name='my_profile'),
    path('add-reward/<int:id>/', views.add_reward, name='add_reward'),
    path('rewards-summary/', views.rewards_summary, name='rewards_summary'),
    path('delete-reward/<int:id>/', views.delete_reward, name='delete_reward'),
    path('edit-reward/<int:id>/', views.edit_reward, name='edit_reward'),
    path('reward-detail/<int:id>/', views.reward_detail, name='reward_detail'),
    
    #RESET PASSWORD
    path('password_reset', 
         authentication_views.PasswordResetView.as_view(template_name="user/password-reset.html"), 
         name="password_reset"),
    #STAR HERE MARCH 3, STYLE THE REMAINING URLS AND VIEWS
    path('password_reset_done',
         authentication_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete', authentication_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

    

]

