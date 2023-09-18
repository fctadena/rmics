from django import forms
from .models import Asset



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_manufacturer', 'asset_model', 'asset_rated_capacity', 'asset_type', 'asset_sub_type', 'asset_drive_details', 'asset_year', 'asset_month', 'asset_image_primary']
        
        widgets = {
            'asset_manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_model': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_rated_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_type': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_sub_type': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_drive_details': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_year': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_month': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_image_primary': forms.FileInput(attrs={'class': 'form-control', 'id':'inputGroupFile01'}),
        }
        