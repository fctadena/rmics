from cfms.models import FindingsLog
from drms.models import MaintenanceLog





def logs_context_kpi_section(request):
    open_findings = FindingsLog.objects.exclude(status='Done').count()
    maintenancelog = MaintenanceLog.objects.all()
    

    context = {
        'open_findings': open_findings,
        'maintenancelog': maintenancelog
    }
    
    return context
