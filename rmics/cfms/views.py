from django.shortcuts import render, redirect
from .models import FindingsLog
from .forms import FindingsLogForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView

# Create your views here.



def cfms(request):
    return render(request, 'rmics/base.html')


def add_findings(request):    
    if request.method == 'POST':
        form = FindingsLogForm(request.POST)
        if form.is_valid():
            findings = form.save()
        return redirect('cfms:findings_summary')
            
    
    else:
        form = FindingsLogForm()
    return render(request, 'cfms/add-findings.html', {'form':form})

# USE THIS TO AS REFERENCE TO CONVERT add_findings to Class view with message succes
# class add_log(CreateView):
#     model = MaintenanceLog
#     form_class = MaintenanceLogForm
#     template_name = 'drms/add-log.html'
    
#     def get_success_url(self):
#         messages.success(self.request, 'ADDED LOG SUCCESSFULLY', extra_tags='success')
#         return reverse_lazy('drms:maintenance_records')


def delete_findings(request, id):
    findingslog = FindingsLog.objects.get(id=id)
    
    if request.method == 'POST':
        findingslog.delete()
        messages.success(request, 'SUCCESSFULLY DELETED FINDINGS LOG', extra_tags='warning')
        return redirect('cfms:findings_summary')
    
    return render(request, 'cfms/delete-findings.html', {'findingslog':findingslog})


class findings_detail(DetailView):
    model = FindingsLog
    template_name = 'cfms/findings-detail.html'


def findings_summary(request):
    logs = FindingsLog.objects.all().order_by('-time_of_discovery')
    return render(request, 'cfms/findings-summary.html', {'logs':logs})

def update_findings(request):
    return render(request, 'cfms/update-findings.html')