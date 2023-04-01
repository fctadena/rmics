from django.db import models
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import request




# Create your models here.



class Asset(models.Model):
    
    def __str__(self):
        return self.asset_manufacturer
    
    
    asset_manufacturer = models.CharField(max_length = 100)
    asset_model = models.CharField(max_length = 100)
    asset_sub_model_01 = models.CharField(max_length=50, blank=True)
    asset_sub_model_02 = models.CharField(max_length=50, blank=True)
    asset_sub_model_03 = models.CharField(max_length=50, blank=True)
    asset_year = models.IntegerField(blank=True)
    asset_month = models.CharField(max_length = 50, blank=True)
    
    def get_absolute_url(self):
        return render(request, template_name='ams/asset-list.html')
    
    
    
    

class Plant(models.Model):
    plant_name = models.CharField(max_length = 100)
    plant_address = models.CharField(max_length = 100)
    plant_business = models.CharField(max_length = 100)
    plant_manager = models.CharField(max_length=100)
    plant_manager_email = models.CharField(max_length=100)
    plant_coordinator = models.CharField(max_length=100)
    plant_coordinator_email = models.CharField(max_length=100)
    
    
#class Modification(models.Model) -> This is a record of all the modificatinos done to the equipment that is not the same as the stock parts. This record is per plant.
#class MaintenanceRecord(models.Model) -> this data is from the daily report where an activity is tag to this equipment from all of the plants. This record is per plant.
    