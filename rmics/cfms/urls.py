from . import views
from django.urls import path



app_name = 'cfms'


urlpatterns = [
    path('', views.cfms, name='cfms_index'),
    path('add-findings/', views.add_findings, name='add_findings'),
    path('delete-findings/<int:id>/', views.delete_findings, name='delete_findings'),
    path('findings-detail/<int:pk>/', views.findings_detail.as_view(), name='findings_detail'),
    path('findings-summary/', views.findings_summary, name='findings_summary'),
    path('update-findings/', views.update_findings, name='update_findings'),
]