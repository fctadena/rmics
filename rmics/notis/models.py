from django.db import models
from notifications.models import Notification as BaseNotification
from django.contrib.auth.models import User

# Create your models here.


class NotificationType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# class Notification(BaseNotification):
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE)
#     notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
#     # Additional fields specific to your notification
