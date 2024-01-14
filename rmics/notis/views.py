from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

# Create your views here.

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'notis/notifications.html', {'notifications': notifications})
