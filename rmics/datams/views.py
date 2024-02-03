from django.shortcuts import render
from drms.models import MaintenanceLog
from cfms.models import FindingsLog
# Create your views here.




def kpi_section(request):
    drms_data = MaintenanceLog.objects.all()
    cfms_data  = FindingsLog.objects.all()
    
    
    
    context = {
        'drms_data':drms_data,
        'cfms_data': cfms_data
    }
    
    return render(template_name="kpi-section.html", context=context)