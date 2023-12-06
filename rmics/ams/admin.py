from django.contrib import admin
from .models import Asset, PlantAssignment

# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ('get_asset_name','asset_manufacturer')


class PlantAssignmentAdmin(admin.ModelAdmin):
    list_display = ('plant', 'plant_code')

admin.site.register(Asset, AssetAdmin)
admin.site.register(PlantAssignment, PlantAssignmentAdmin)
