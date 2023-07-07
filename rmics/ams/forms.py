from django import forms
from .models import Asset



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_manufacturer', 'asset_model', 'asset_sub_model_01', 'asset_sub_model_02', 'asset_sub_model_03', 'asset_year', 'asset_month', 'asset_image_primary']
        
        widgets = {
            'asset_manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_model': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_sub_model_01': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_sub_model_02': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_sub_model_03': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_year': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_month': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_image_primary': forms.FileInput(attrs={'class': 'form-control', 'id':'inputGroupFile01'}),
        }
        
        
        
        
        # labels = {
        #     'asset_manufacturer': 'Manufacturer',
        #     'asset_model': 'Model',
        #     'asset_sub_model_01': 'Sub-model 1',
        #     'asset_sub_model_02': 'Sub-model 2',
        #     'asset_sub_model_03': 'Sub-model 3',
        #     'asset_year': 'Year',
        #     'asset_month': 'Month',
        #     'asset_image_primary': 'Asset Image',
        # }