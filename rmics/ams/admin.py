from django.contrib import admin
from .models import Asset

# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_manufacturer', 'asset_model', 'asset_sub_model_01', 'asset_sub_model_02', 'asset_sub_model_03', 'asset_year', 'asset_month', 'asset_image_primary')

admin.site.register(Asset, AssetAdmin)
