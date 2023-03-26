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
    asset_sub_model_01 = models.CharField(max_length=50)
    asset_sub_model_02 = models.CharField(max_length=50)
    asset_sub_model_03 = models.CharField(max_length=50)
    asset_year = models.IntegerField()
    asset_month = models.CharField(max_length = 50)
    
    def get_absolute_url(self):
        return render(request, template_name='ams/asset-list.html')
    
    
    
    

class Plant(models.Model):
    plant_name = models.CharField(max_length = 100)
    plant_address = models.CharField(max_length = 100)
    plant_business = models.CharField(max_length = 100)
    
    