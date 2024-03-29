from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ams.models import Asset, PlantAssignment
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone




class MaintenanceLog(models.Model):
    wo_seq_num = models.BigIntegerField(validators=[MinValueValidator(1, message="WORK SEQ NUM must be a positive number")], blank=True, null=True)
    machine_failure_breakdown = models.CharField(max_length=255, blank=True, null=True)
    description_of_work = models.TextField(max_length=600, blank=True, null=True)
    work_type = models.CharField(max_length=50, choices=[('Repair', 'Repair'), ('Preventive Maintenance', 'Preventive Maintenance'), ('Fabrication', 'Fabrication'), ('Equipment Setup', 'Equipment Setup'), ('General Jobs', 'General Jobs')], blank=True, null=True)
    root_cause = models.TextField(max_length=600, blank=True, null=True)
    job_start = models.DateTimeField(blank=True, null=True)
    job_end = models.DateTimeField(blank=True, null=True)
    time_consumed = models.DurationField(blank=True, null=True) 
    affecting_production = models.DurationField(blank=True, null=True) 
    affecting_time = models.DurationField(blank=True, null=True)
    equipment_name = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='maintenance_logs_equipment', blank=True, null=True)
    equipment_code = models.CharField(max_length=255, blank=True, null=True)
    section = models.CharField(max_length=255, blank=True, null=True)
    system = models.CharField(max_length=100, choices=[('Process', 'Process'), ('Civil', 'Civil'), ('Auxiliary', 'Auxiliary'), ('Plant Water', 'Plant Water'), ('Power', 'Power'), ('Steam', 'Steam'), ('Compressed Air', 'Compressed Air'), ('FFW', 'FFW')], default='Process', blank=True, null=True)
    affecting_bagging = models.BooleanField(default=False, blank=True)
    machine_failure = models.BooleanField(default=False, blank=True)
    type_of_stop_time = models.CharField(max_length=20, choices=[('Planned', 'Planned'), ('Unplanned', 'Unplanned')], default=None, blank=True, null=True)
    work_center = models.CharField(max_length=100, choices=[('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Instrumentation & Controls', 'Instrumentation & Controls'), ('Fabrication', 'Fabrication'), ('Lubrication', 'Lubrication')], default=None, blank=True, null=True)
    personnel_assigned = models.CharField(max_length=255, blank=True, null=True)
    parts_replaced = models.CharField(max_length=255, blank=True, null=True)
    quantity_of_parts = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Waiting for Parts', 'Waiting for Parts'), ('On-going', 'On-going'), ('Completed', 'Completed'), ('Pending', 'Pending')], default=None, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    spare_details = models.TextField(blank=True, null=True)
    notification_num = models.CharField(max_length=255, blank=True, null=True)
    include_log = models.BooleanField(default=True, blank=True)
    plant_of_record = models.ForeignKey(PlantAssignment, on_delete=models.CASCADE, related_name='maintenance_logs', blank=True, null=True)
    log_reporter = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
 
    
    def __str__(self):
        return f"{self.machine_failure_breakdown} - {self.equipment_name}"



class MaintenanceLogComment(models.Model):
    maintenance_log = models.ForeignKey(MaintenanceLog, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('timestamp',)
        
    
    def __str__(self):
        return self.comment_text


class PlantData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    planned_production_time = models.DurationField(validators=[MaxValueValidator(limit_value=timezone.timedelta(hours=24))])
    output = models.IntegerField(blank=True, null=True)
    output_unit = models.CharField(max_length=20, choices=[('Bags', 'Bags'), ('Liters', 'Liters'), ('Barrels', 'Barrels')], default=None, blank=True, null=True)
    plant_of_record = models.ForeignKey(PlantAssignment, on_delete=models.CASCADE, related_name='plant_data', blank=True, null=True)
    log_reporter = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return f"{self.planned_production_time} - {self.output} {self.output_unit} | from {self.plant_of_record} by {self.log_reporter}"