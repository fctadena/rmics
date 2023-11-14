from django.shortcuts import render
from .models import FindingsLog
from .forms import FindingsLogForm
from django.http import HttpResponse

# Create your views here.



def cfms(request):
    return render(request, 'rmics/base.html')


def add_findings(request):    
    if request.method == 'POST':
        form = FindingsLogForm(request.POST)
        if form.is_valid():
            findings = form.save()
            return HttpResponse('Successfully added form')
    
    else:
        form = FindingsLogForm()
    return render(request, 'cfms/add-findings.html', {'form':form})



def delete_findings(request):
    return render(request, 'cfms/delete-findings.html')

def findings_detail(request):
    return render(request, 'cfms/findings-detail.html')

def findings_summary(request):
    logs = FindingsLog.objects.all()
    
    return render(request, 'cfms/findings-summary.html', {'logs':logs})

def update_findings(request):
    return render(request, 'cfms/update-findings.html')