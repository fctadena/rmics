from django.shortcuts import render, redirect
from .models import MaintenanceLog
from django.views.generic.edit import CreateView
from .forms import MaintenanceLogForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

#IMPORTS FOR THE HANDLER
from django.views import View
from .models import MaintenanceLog
from ams.models import Asset



# Create your views here.

def drms(request):
    return render(request, 'rmics/base.html')


#CRUD STARTS HERE
class log_detail(DetailView):
    model = MaintenanceLog
    template_name = 'drms/log-detail.html'


def delete_log(request,id):
    log = MaintenanceLog.objects.get(id=id)
    
    if request.method == 'POST':
        log.delete()
        messages.success(request, 'DELETED LOG SUCCESSFULLY', extra_tags='warning')
        return redirect('drms:maintenance_records')
    
    return render(request, 'drms/delete-log.html', {'log':log})


def update_log(request,id):
    log = MaintenanceLog.objects.get(id=id)
    
    if request.method == 'POST':
        form = MaintenanceLogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            messages.success(request, 'UPDATED LOG SUCCESSFULLY', extra_tags='info')
            return redirect('drms:maintenance_records')
    else:
        form = MaintenanceLogForm(instance=log)
    return render(request, 'drms/update-log.html', {'form':form, 'log':log})
    
    


def maintenance_records(request):
    maintenance_log = MaintenanceLog.objects.all().order_by('-job_start')
    return render(request, 'drms/maintenance-records.html', {'maintenance_log':maintenance_log})


class add_log(CreateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'drms/add-log.html'
    
    def get_success_url(self):
        messages.success(self.request, 'ADDED LOG SUCCESSFULLY', extra_tags='success')
        return reverse_lazy('drms:maintenance_records')
    

#ERROR HANDLER
# def update_records_view(request):
#     template_name = 'drms/update-log.html'

#     if request.method == 'GET':
#         return render(request, template_name)
#     elif request.method == 'POST':
#         try:
#             # Update logic
#             maintenance_logs = MaintenanceLog.objects.filter(equipment_name__isnull=False)
            
#             for log in maintenance_logs:
#                 log.equipment_name = None
#                 log.save()

#             # Display success message
#             messages.success(request, 'Records updated successfully.')
#         except Exception as e:
#             # Display error message if update fails
#             messages.error(request, f'An error occurred: {str(e)}')

#         return redirect('drms:update_log')