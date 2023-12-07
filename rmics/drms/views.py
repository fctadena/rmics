from django.shortcuts import render, redirect
from .models import MaintenanceLog
from django.views.generic.edit import CreateView
from .forms import MaintenanceLogForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

#IMPORTS FOR THE HANDLER
from django.views import View
from ams.models import Asset
from user.models import CustomUserProfile



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

    def form_valid(self, form):
        # Get the current user and their associated CustomUserProfile
        current_user = self.request.user
        user_profile = CustomUserProfile.objects.get(user=current_user)
        
        # Set the log_reporter field to the current user and plant_assignment
        form.instance.log_reporter = current_user
        form.instance.plant_of_record = user_profile.plant_assignment
        
        # Call the form_valid method of the parent class to save the instance
        response = super().form_valid(form)

        # Add a success message
        messages.success(self.request, 'ADDED LOG SUCCESSFULLY', extra_tags='success')

        return response

    def get_success_url(self):
        return reverse_lazy('drms:maintenance_records')

    
    
# COPY OF OLD add_log view
# class add_log(CreateView):
#     model = MaintenanceLog
#     form_class = MaintenanceLogForm
#     template_name = 'drms/add-log.html'
    
#     def get_success_url(self):
#         messages.success(self.request, 'ADDED LOG SUCCESSFULLY', extra_tags='success')
#         return reverse_lazy('drms:maintenance_records')
    


# EXAMPLE TO FILTER LOGS THAT CURRENT USER WAS CREATOR
# def my_purchases(request):
#     orders = OrderDetail.objects.filter(customer_email=request.user.email)
    
#     context = {
#         'orders':orders
#     }
#     return render(request, 'main/purchases.html', context)



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


def test_view(request):
    if request.method == "GET":
        current_user = request.user
        
        context = {
            'current_user':current_user
        }
        return render(request, 'drms/test.html', context)
        
    