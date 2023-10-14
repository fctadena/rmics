from django import forms
from .models import MaintenanceLog



class MaintenanceLogForm(forms.ModelForm):
    class Meta:
            model = MaintenanceLog
            fields = [
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
            
    

# class MaintenanceLogForm(forms.ModelForm):
#     class Meta:
#         model = MaintenanceLog
#         fields = '__all__'
#         widgets = {
#             'job_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'job_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
        
#     # Custom widget for DurationField in hh:mm format
#     time_consumed = forms.CharField(
#         label='Time Consumed (hh:mm)',
#         widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
#     )
    
#     affecting_production = forms.CharField(
#         label='Affecting Production (hh:mm)',
#         widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
#     )
    
#     affecting_time = forms.CharField(
#         label='Affecting Time (hh:mm)',
#         widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
#     )

#     # Override the save method to handle DurationField conversion
#     def save(self, commit=True):
#         instance = super().save(commit=False)
        
#         # Convert hh:mm strings to timedelta objects
#         instance.time_consumed = self.cleaned_data.get('time_consumed')
#         instance.affecting_production = self.cleaned_data.get('affecting_production')
#         instance.affecting_time = self.cleaned_data.get('affecting_time')

#         if commit:
#             instance.save()
#         return instance
