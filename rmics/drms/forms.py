from django import forms
from .models import MaintenanceLog, PlantData



class MaintenanceLogForm(forms.ModelForm):
    class Meta:
            model = MaintenanceLog
            fields = [
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
                'include_log'
                ]
            
            
class PlantDataForm(forms.ModelForm):
    
    class Meta:
        model = PlantData
        fields = '__all__'