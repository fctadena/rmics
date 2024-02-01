from . import views
from django.urls import path



app_name = 'drms'


urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications'),
]