from .models import FindingsLog


def findings_log_list_context(request):
    findings_log = FindingsLog.objects.all().order_by('-timestamp')[:5]
    
    context = {
        'findings_log':findings_log
    }
    return context