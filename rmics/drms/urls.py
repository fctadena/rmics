from . import views
from django.urls import path



app_name = 'drms'


urlpatterns = [
    path('', views.drms, name='drms_index'),
    path('daily-report/', views.daily_report, name='daily_report'),
    path('log-detail/', views.log_detail, name='log_detail'),
    path('add-log/', views.add_log.as_view(), name='add_log'),
    path('delete-log/', views.delete_log, name='delete_log'),
    path('update-log/', views.update_log, name='update_log'),
]
