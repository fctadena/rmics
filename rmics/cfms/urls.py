from . import views
from django.urls import path



app_name = 'cfms'


urlpatterns = [
    path('', views.cfms, name='cfms_index'),
    path('add-findings/', views.add_findings, name='add_findings'),
    path('delete-findings/', views.delete_findings, name='delete_findings'),
    path('findings-detail/', views.findings_detail, name='findings_detail'),
    path('findings-summary/', views.findings_summary, name='findings_summary'),
    path('update-findings/', views.update_findings, name='update_findings'),
]