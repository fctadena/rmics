from django.contrib import admin
from .models import Asset, PlantAssignment

# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_manufacturer', 'asset_rated_capacity', 'asset_model', 'asset_type', 'asset_sub_type', 'asset_drive_details', 'asset_year', 'asset_month', 'asset_image_primary')


class PlantAssignmentAdmin(admin.ModelAdmin):
    list_display = ('plant', 'plant_code')

admin.site.register(Asset, AssetAdmin)
admin.site.register(PlantAssignment, PlantAssignmentAdmin)
