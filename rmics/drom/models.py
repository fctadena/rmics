from django.db import models

# Create your models here.



class daily_report_om(models.Model):
    date = models.CharField(max_length = 100)
    plant = models.CharField(max_length = 100) #with pre-determined values (BMP MisOr1, BMP Bukidnon, etc.)
    planned_production_time = models.CharField(max_length = 100)
    manpower_1st_shift = models.CharField(max_length = 100)
    manpower_2nd_shift = models.CharField(max_length = 100)
    manpower_3rd_shift = models.CharField(max_length = 100)
    rest_day = models.CharField(max_length = 100)
    on_leave = models.CharField(max_length = 100)
    downtime_summary_line1 = models.CharField(max_length = 100)
    downtime_summary_line2 = models.CharField(max_length = 100)
    downtime_summary_line3 = models.CharField(max_length = 100)
    downtime_summary_line4 = models.CharField(max_length = 100)
    downtime_summary_line5 = models.CharField(max_length = 100)
    downtime_summary_line6 = models.CharField(max_length = 100)
    day_status_line1 = models.CharField(max_length = 100)
    day_status_line2 = models.CharField(max_length = 100)
    day_status_line3 = models.CharField(max_length = 100)
    day_status_line4 = models.CharField(max_length = 100)
    day_status_line5 = models.CharField(max_length = 100)
    day_status_line6 = models.CharField(max_length = 100)
    health_issues = models.CharField(max_length = 100)
    safety_issues = models.CharField(max_length = 100)
    other_issues = models.CharField(max_length = 100)

    


