from django import forms
from .models import Asset



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_manufacturer', 'asset_model', 'asset_sub_model_01', 'asset_sub_model_02', 'asset_sub_model_03', 'asset_year', 'asset_month']
        labels = {
            'asset_manufacturer': 'Manufacturer',
            'asset_model': 'Model',
            'asset_sub_model_01': 'Sub-model 1',
            'asset_sub_model_02': 'Sub-model 2',
            'asset_sub_model_03': 'Sub-model 3',
            'asset_year': 'Year',
            'asset_month': 'Month',
        }