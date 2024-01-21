from django.db.models.signals import post_save
from notifications.signals import notify
from cfms.models import FindingsLog
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from user.models import Reward
from ams.models import Asset
from drms.models import MaintenanceLog




# CRITIFCAL FINDINGS CREATION AND UPDATE SIGNAL
@receiver(post_save, sender=FindingsLog)            
def critical_findings_created(instance, created, **kwargs):
    print("Signal received!")
    if created:
        print("Signal for Created FindingsLog Triggered")
        # Assuming instance.log_reporter is the user you want to notify
        # Modify this logic based on your actual requirements
        recipient_users = []

        # Check user's group and add to recipient_users accordingly
        for group_name in ['Operations Analyst Super', 'Operations Analyst', 'National Management']:
            group = Group.objects.get(name=group_name)
            users_in_group = group.user_set.all()
            recipient_users.extend(users_in_group)

        # Send notification to the specified group
        notify.send(sender=instance, recipient=recipient_users, verb="Critical finding has been CREATED.")
        print("A critical finding has been CREATED")
    
    else:
        print("Signal for Updating FindingsLog Triggered")
        recipient_users = []
        # Check user's group and add to recipient_users accordingly
        for group_name in ['Operations Analyst Super', 'Operations Analyst', 'National Management']:
            group = Group.objects.get(name=group_name)
            users_in_group = group.user_set.all()
            recipient_users.extend(users_in_group)

        # Send notification to the specified group
        notify.send(sender=instance, recipient=recipient_users, verb="Critical finding has been UPDATED.")
        print("A critical finding has been UPDATED")
        
        
        
# NEW EMPLOYEE ADDED SIGNAL
@receiver(post_save, sender=User)            
def new_employee_added(instance, created, **kwargs):
    print("Signal received!")
    if created:
        print("Signal for New Employee (User) Triggered")
        recipient_users = User.objects.all()

        # Send notification to the specified group
        notify.send(sender=instance, recipient=recipient_users, verb="A new team member is ADDED!")
        print("A new team member is ADDED!")
        
        
        
# AN AWARD IS GIVEN TO AN EMPLOYEE SIGNAL
@receiver(post_save, sender=Reward)            
def new_employee_award_added(instance, created, **kwargs):
    print("Signal received!")
    if created:
        print("Signal for New Award Triggered")
        recipient_users = User.objects.all()

        # Send notification to the specified group
        notify.send(sender=instance, recipient=recipient_users, verb="A NEW AWARD is given to an one of our team members!")
        print("A NEW AWARD is given to an one of our team members!")
        
        
# NEW ASSET ADDED SIGNAL
@receiver(post_save, sender=Asset)            
def new_asset_added(instance, created, **kwargs):
    print("Signal received!")
    if created:
        print("Signal for New Asset Added Triggered")
        recipient_users = User.objects.all()

        # Send notification to the specified group
        notify.send(sender=instance, recipient=recipient_users, verb="A NEW ASSET has been ADDED.")
        print("A NEW ASSET has been ADDED.")
        


# CORRECTIVE MAINTENANCE LOG HAS BEEN ADDED TO A CRITICAL ASSET
@receiver(post_save, sender=MaintenanceLog)            
def critical_findings_created(instance, created, **kwargs):
    print("Signal received!")
    if created and instance.work_type == "Repair" and instance.equipment_name.critical_asset_designation == True or (instance.work_type == "Repair" and instance.equipment_name.critical_asset_designation == True):
        print("Signal for Corrective Maintenance Log for a Critical Asset Triggered")
        recipient_users = []

        for group_name in ['Operations Analyst Super', 'Operations Analyst', 'National Management']:
            group = Group.objects.get(name=group_name)
            users_in_group = group.user_set.all()
            recipient_users.extend(users_in_group)

        notify.send(sender=instance, recipient=recipient_users, verb="New Corrective Maintenance Log for a CRITICAL ASSET ADDED")
        print("New Corrective Maintenance Log for a CRITICAL ASSET ADDED")
    
    
# A MAINTENANCE LOG WITH AFFECTING BAGGING AS TRUE
@receiver(post_save, sender=MaintenanceLog)            
def maintenance_log_affecting_bagging(instance, created, **kwargs):
    print("Signal received!")
    if created and instance.affecting_bagging == True or (instance.affecting_bagging == True):
        print("Signal for MAINTENANCE LOG WITH AFFECTING BAGGING AS TRUE Triggered")
        recipient_users = []

        for group_name in ['Operations Analyst Super', 'Operations Analyst', 'National Management']:
            group = Group.objects.get(name=group_name)
            users_in_group = group.user_set.all()
            recipient_users.extend(users_in_group)

        notify.send(sender=instance, recipient=recipient_users, verb="A MAINTENANCE LOG WITH AFFECTING BAGGING IS RECORDED")
        print("A MAINTENANCE LOG WITH AFFECTING BAGGING IS RECORDED")