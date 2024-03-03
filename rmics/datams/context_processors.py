from cfms.models import FindingsLog
from drms.models import MaintenanceLog
from django.contrib.auth.models import Group
from django.contrib.auth.models import AnonymousUser


    
def logs_context_kpi_section(request):
    user = request.user
    
    # Check if the user is logged in
    if isinstance(user, AnonymousUser):
        # User is not authenticated, set open_findings to a default value
        open_findings = 0
    else:
        # Define target groups
        target_groups = ["Operations Analyst", "Operations Analyst Super", "National Management"]
        
        # Check if the user is in any of the target groups
        if user.groups.filter(name__in=target_groups).exists():
            open_findings = FindingsLog.objects.exclude(status='Done').count()
        else:
            open_findings = FindingsLog.objects.exclude(status='Done').filter(log_reporter=user).count()
    
    maintenancelog = MaintenanceLog.objects.all()
    
    context = {
        'open_findings': open_findings,
        'maintenancelog': maintenancelog
    }
    
    return context






















# def logs_context_kpi_section(request):
        
#     open_findings = FindingsLog.objects.exclude(status='Done').count()
#     maintenancelog = MaintenanceLog.objects.all()
    
#     context = {
#         'open_findings': open_findings,
#         'maintenancelog': maintenancelog
#     }
    
#     return context