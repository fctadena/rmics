from django.db.models.signals import post_save
from notifications.signals import notify
from cfms.models import FindingsLog
from django.dispatch import receiver



@receiver(post_save, sender=FindingsLog)
def critical_findings_created(sender, instance, created, **kwargs):
    notify.send(instance, verb='was created')
    print("A new Crifical Findings was created")

post_save.connect(critical_findings_created, sender=FindingsLog)


# CONTINUE IMPLEMENT THIS ##
# https://www.advantch.com/blog/how-to-set-up-user-notifications-for-your-django-app-part-1/
# https://pypi.org/project/django-notifications-hq/



