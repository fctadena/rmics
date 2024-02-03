from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import MaintenanceLog, MaintenanceLogComment, PlantData
from django.views.generic.edit import CreateView
from .forms import MaintenanceLogForm, PlantDataForm, MaintenanceLogCommentForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

#NOTIFS
from notifications.signals import notify


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
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = MaintenanceLogCommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = MaintenanceLogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.maintenance_log = self.get_object()
            comment.commenter = request.user  # Assuming you have user authentication
            comment.save()
            return redirect('drms:log_detail', pk=self.get_object().pk)
        else:
            # Handle invalid form submission if needed
            pass
        
        



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
        user = request.user #FOR NOTIFS TESTING
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            notify.send(user, recipient=request.user, verb='A LOG HAS BEEN UPDATED')#FOR NOTIFS TESTING
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
    
    


    



#THIS LACK LOGIC TO PREVENT USER FROM ADDING NEW PLANTRECORD WITHIN THE DAY
def add_plant_data(request):
    
    current_user = request.user
    user_details = CustomUserProfile.objects.get(user=current_user)
    plant_data_form = PlantDataForm
    
    
    if request.method == "POST": 
        plant_data_form = PlantDataForm(request.POST)        
        
        if plant_data_form.is_valid():
            plant_data_form.save()
            messages.success(self.request, 'ADDED PLANT DATA SUCCESSFULLY', extra_tags='success')
            return redirect('drms:plant_data_summary')
        
        else:
            print("FORM NOT VALID")
             
        
    else:
        print("THIS IS A GET REQUEST")

        plant_data_form = PlantDataForm()
        plant_data_form.fields['log_reporter'].initial = current_user
        plant_data_form.fields['plant_of_record'].initial = user_details.plant_assignment
        
                
        context = {
            'plant_data_form':plant_data_form
        }
    
        return render(request, template_name="drms/add-plant-data.html", context=context)





def edit_plant_data(request, id):
    
    plant_data = PlantData.objects.get(id=id)
    
    if request.method == "POST":
        form = PlantDataForm(request.POST, instance=plant_data)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'UPDATED PLANT DATA SUCCESSFULLY', extra_tags='info')
            return redirect('drms:plant_data_summary')
        
        else:
            return HttpResponse("THIS IS AN ERRROR")
    
    else:
        
        form = PlantDataForm(instance=plant_data)
        
        context = {
            
            'form':form
        }
        
        return render(request, template_name="drms/edit-plant-data.html", context=context)



def plant_data_summary(request):
    
    plant_data_summary = PlantData.objects.all()

    context = {
        'plant_data_summary':plant_data_summary
    }
    
    return render(request, template_name="drms/plant-data-summary.html", context=context)







def plant_data(request, id):
    plant_data = PlantData.objects.get(id=id)
    
    
    context = {
        'plant_data':plant_data,
 
    }
    return render(request, template_name="drms/plant-data.html", context=context)

    







# def add_plant_data(request):
#     current_user = request.user
#     user_details = CustomUserProfile.objects.get(user=current_user)
#     plant_data_form = PlantDataForm
    
#     if request.method == "POST": 
#         plant_data_form = PlantDataForm(request.POST)        
        
#         if plant_data_form.is_valid():
#             # Check if a PlantData instance with the same timestamp already exists
#             timestamp = plant_data_form.cleaned_data.get('timestamp')
#             if timestamp:
#                 existing_instance = PlantData.objects.filter(timestamp__date=timestamp.date(), log_reporter=current_user).first()

#                 if existing_instance:
#                     # Raise an error or handle it as per your requirements
#                     plant_data_form.add_error('timestamp', 'You already added data for this day.')
#                     print("ERROR: Data already exists for this day.")
#                     return render(request, template_name="drms/add-plant-data.html", context={'plant_data_form': plant_data_form})
#                 else:
#                     # Save the new PlantData instance
#                     plant_data_form.save()
#                     return redirect('drms:plant_data_summary')
        
#         else:
#             print("FORM NOT VALID")
         
#     else:
#         print("THIS IS A GET REQUEST")

#         plant_data_form = PlantDataForm()
#         plant_data_form.fields['log_reporter'].initial = current_user
#         plant_data_form.fields['plant_of_record'].initial = user_details.plant_assignment
                
#     context = {
#         'plant_data_form': plant_data_form
#     }

#     return render(request, template_name="drms/add-plant-data.html", context=context)











def test_view(request):
    if request.method == "GET":
        current_user = request.user
        
        context = {
            'current_user':current_user
        }
        return render(request, 'drms/test.html', context)
        
    