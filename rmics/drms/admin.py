from django.contrib import admin
from .models import MaintenanceLog

# Register your models here.


class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = (
        'wo_seq_num',
        'machine_failure_breakdown',
        'description_of_work',
        'work_type',
        'root_cause',
        'job_start',
        'job_end',
        'time_consumed',
        'affecting_production',
        'affecting_time',
        'equipment_name',
        'equipment_code',
        'section',
        'system',
        'affecting_bagging',
        'machine_failure',
        'type_of_stop_time',
        'work_center',
        'personnel_assigned',
        'parts_replaced',
        'quantity_of_parts',
        'status',
        'remarks',
        'spare_details',
        'notification_num',
        'include_log',
    )


admin.site.register(MaintenanceLog, MaintenanceLogAdmin)

    