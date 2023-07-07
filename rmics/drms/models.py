from django.db import models

# Create your models here.


from django.db import models

class MaintenanceLog(models.Model):
    wo_seq_num = models.CharField(max_length=255)
    machine_failure_breakdown = models.CharField(max_length=255)
    description_of_work = models.TextField()
    work_type = models.CharField(max_length=50, choices=[('Repair', 'Repair'), ('Preventive Maintenance', 'Preventive Maintenance'), ('Fabrication', 'Fabrication'), ('General Jobs', 'General Jobs')])
    root_cause = models.TextField()
    job_start = models.DateTimeField()
    job_end = models.DateTimeField()
    time_consumed = models.DurationField()
    affecting_production = models.DurationField()
    affecting_time = models.DurationField()
    equipment_name = models.CharField(max_length=255)
    equipment_code = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    affecting_bagging = models.BooleanField()
    machine_failure = models.BooleanField()
    type_of_stop_time = models.CharField(max_length=20, choices=[('Planned', 'Planned'), ('Unplanned', 'Unplanned')])
    work_center = models.CharField(max_length=50, choices=[('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Instrumentation & Controls', 'Instrumentation & Controls'), ('Fabrication', 'Fabrication'), ('Lubrication', 'Lubrication')])
    personnel_assigned = models.CharField(max_length=255)
    parts_replaced = models.CharField(max_length=255)
    quantity_of_parts = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Waiting for Parts', 'Waiting for Parts'), ('On-going', 'On-going'), ('Completed', 'Completed'), ('Pending', 'Pending')])
    remarks = models.TextField()
    spare_details = models.TextField()
    notification_num = models.CharField(max_length=255)
