from django.shortcuts import render
from .models import MaintenanceLog
from django.views.generic.edit import CreateView
from .forms import MaintenanceLogForm
from django.contrib import messages
from django.urls import reverse_lazy



# Create your views here.


def drms(request):
    return render(request, 'rmics/drms-base.html')


def daily_report(request):
    return render(request, 'drms/daily-report.html')

def log_detail(request):
    return render(request, 'drms/log-detail.html')


#ADDING LOG


def delete_log(request):
    return render(request, 'drms/delete-log.html')

def update_log(request):
    return render(request, 'drms/update-log.html')


def maintenance_records(request):
    model = MaintenanceLog
    
    return render(request, 'drms/maintenance-records.html', )

def maintenance_records(request):
    maintenance_log = MaintenanceLog.objects.all()
    return render(request, 'drms/maintenance-records.html', {'maintenance_log':maintenance_log})





class add_log(CreateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'drms/add-log.html'
    
    def get_success_url(self):
        messages.success(self.request, 'ADDED LOG SUCCESSFULLY', extra_tags='success')
        return reverse_lazy('drms:maintenance_records')