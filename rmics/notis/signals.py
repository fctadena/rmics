from django.db.models.signals import post_save
from notifications.signals import notify
from cfms.models import FindingsLog
from django.dispatch import receiver




# @receiver(post_save, sender=FindingsLog)
# #POSSIBLE PROBLEM, CFMS FindingsLog model must have a field called reporter, or the one who created the log as well as plant.
    
# def critical_findings_created(sender, instance, created, **kwargs):
#     print("Signal received!")
#     if created:
#         notify.send(sender=instance, recipient=, verb="A critical finding has been added")
#         print("A new Critical Finding was created")

# post_save.connect(critical_findings_created, sender=FindingsLog)
