from django import forms
from .models import MaintenanceLog


class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'
        widgets = {
            'job_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'job_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    # Custom widget for DurationField in hh:mm format
    time_consumed = forms.CharField(
        label='Time Consumed (hh:mm)',
        widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
    )
    
    affecting_production = forms.CharField(
        label='Affecting Production (hh:mm)',
        widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
    )
    
    affecting_time = forms.CharField(
        label='Affecting Time (hh:mm)',
        widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}),
    )

    # Override the save method to handle DurationField conversion
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Convert hh:mm strings to timedelta objects
        instance.time_consumed = self.cleaned_data.get('time_consumed')
        instance.affecting_production = self.cleaned_data.get('affecting_production')
        instance.affecting_time = self.cleaned_data.get('affecting_time')

        if commit:
            instance.save()
        return instance



# class MaintenanceLogForm(forms.ModelForm):
#     class Meta:
#         model = MaintenanceLog
#         fields = '__all__'
#         widgets = {
#             'job_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'job_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'time_consumed': forms.TextInput(attrs={'readonly': True}),
#             'affecting_production': forms.TextInput(attrs={'readonly': True}),
#             'affecting_time': forms.TextInput(attrs={'readonly': True}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         job_start = cleaned_data.get('job_start')
#         job_end = cleaned_data.get('job_end')

#         if job_start and job_end:
#             if job_end <= job_start:
#                 raise forms.ValidationError('Job end time should be greater than job start time.')
            
#             cleaned_data['time_consumed'] = job_end - job_start
#             cleaned_data['affecting_production'] = cleaned_data.get('affecting_production') or cleaned_data['time_consumed']
#             cleaned_data['affecting_time'] = cleaned_data.get('affecting_time') or cleaned_data['time_consumed']

#         return cleaned_data



