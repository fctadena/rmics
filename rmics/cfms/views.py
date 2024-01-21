from django.shortcuts import render, redirect
from .models import FindingsLog
from .forms import FindingsLogForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from user.decorators import unauthenticated_logic, allowed_groups
from django.utils.decorators import method_decorator



def cfms(request):
    return render(request, 'rmics/base.html')


@method_decorator(unauthenticated_logic, name="dispatch")
@method_decorator(allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management']), name="dispatch")
class add_findings(CreateView):
    model = FindingsLog
    form_class = FindingsLogForm
    template_name = 'cfms/add-findings.html'
    
    def form_valid(self, form):
        # Set the log_reporter field to the currently logged-in user
        form.instance.log_reporter = self.request.user
        return super().form_valid(form)
        
        
    def get_success_url(self):
        messages.success(self.request, 'ADDED FINDINGS SUCCESSFULLY', extra_tags='success')
        return reverse_lazy('cfms:findings_summary')

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management'])
def delete_findings(request, id):
    findingslog = FindingsLog.objects.get(id=id)
    
    if request.method == 'POST':
        findingslog.delete()
        messages.success(request, 'SUCCESSFULLY DELETED FINDINGS LOG', extra_tags='warning')
        return redirect('cfms:findings_summary')
    
    return render(request, 'cfms/delete-findings.html', {'findingslog':findingslog})

@method_decorator(unauthenticated_logic, name="dispatch")
class findings_detail(DetailView):
    model = FindingsLog
    template_name = 'cfms/findings-detail.html'

@unauthenticated_logic
def findings_summary(request):
    logs = FindingsLog.objects.all().order_by('-time_of_discovery')
    return render(request, 'cfms/findings-summary.html', {'logs':logs})



@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management'])
def update_findings(request, id):
    findings = FindingsLog.objects.get(id=id)
    
    if request.method == "POST":
        form = FindingsLogForm(request.POST, instance=findings)
        if form.is_valid():
            findings = form.save(commit=False)
            findings.save()
            messages.success(request, 'UPDATED FINDINGS SUCCESSFULLY', extra_tags='info')
            return redirect('cfms:findings_summary')
    
    else:
        form = FindingsLogForm(instance=findings)
        
    context = {
        'findings':findings,
        'form':form,
        'findings':findings
    }
        
    
    return render(request, 'cfms/update-findings.html', context)