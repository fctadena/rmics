from django import forms
from .models import Asset



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_manufacturer', 'asset_model', 'asset_sub_model_01', 'asset_sub_model_02', 'asset_sub_model_03', 'asset_year', 'asset_month']
        