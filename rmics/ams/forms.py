from django import forms
from .models import Asset, PlantAssignment


class AssetForm(forms.ModelForm):
    class Meta:
            model = Asset
            fields = ['asset_manufacturer', 'asset_model', 'asset_rated_capacity', 'asset_type', 'asset_sub_type', 'asset_drive_details', 'asset_year', 'asset_month', 'asset_image_primary']
      
       
        
       
       
       
class PlantForm(forms.ModelForm):
    class Meta:
        model = PlantAssignment
        fields = ['plant', 'plant_code']
       
       
        