from django import forms
from .models import Asset



class AssetForm(forms.ModelForm):
    
    
        
    # widgets = {
    #             'asset_manufacturer': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_model': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_rated_capacity': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_type': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_sub_type': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_drive_details': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_year': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_month': forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
    #             'asset_image_primary': forms.FileInput(attrs={'class': 'input', 'id':'inputGroupFile01'}),
    #         }
    
    
    class Meta:
            model = Asset
            fields = ['asset_manufacturer', 'asset_model', 'asset_rated_capacity', 'asset_type', 'asset_sub_type', 'asset_drive_details', 'asset_year', 'asset_month', 'asset_image_primary']
      
        
    # asset_manufacturer = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))
    
    
    # asset_model = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_rated_capacity = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_type = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_sub_type = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_drive_details = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_year = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    # asset_month = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",
    #     "type": "text",
    #     "placeholder": "",
    # }))

    
    # asset_image_primary = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "input",        
    #     "type": "file",
    #     "data-role": "magic-overlay",
    #     "data-target": "#pictureBtn",
    #     "data-edit": "insertImage",
    # }))
    
    
    
    
    
    # widgets = {
    #         'asset_manufacturer': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_model': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_rated_capacity': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_type': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_sub_type': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_drive_details': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_year': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_month': forms.CharField(attrs={'class': 'input', 'type': 'text', 'placeholder': ''}),
    #         'asset_image_primary': forms.FileInput(attrs={'class': 'input', 'id':'inputGroupFile01'}),
    #     }
        

        
       
       
       
       
       
       
        