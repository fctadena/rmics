from . import views
from django.urls import path



app_name = 'drms'


urlpatterns = [
    path('', views.drms, name='drms_index'),
    path('log-detail/<int:pk>/', views.log_detail.as_view(), name='log_detail'),
    path('add-log/', views.add_log.as_view(), name='add_log'),
    path('delete-log/<int:id>/', views.delete_log, name='delete_log'),
    path('update-log/<int:id>/', views.update_log, name='update_log'),
    path('maintenance-records/', views.maintenance_records, name='maintenance_records'),
    path('test/', views.test_view, name='test'),
]