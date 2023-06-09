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
    asset_image_primary = models.ImageField(upload_to='pics', default='D:\Legacy Projects\rmics\rmics\media\dphd_1.jpg')
    
    def get_absolute_url(self):
        return render(request, template_name='ams/asset-list.html')
    

    
