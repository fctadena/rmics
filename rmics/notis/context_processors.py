from notifications.models import Notification


def notification_list_context(request):
    notifications = Notification.objects.all().order_by('-timestamp')[:5]
    
    
    context = {
        'notifications':notifications
    }
    
    return context