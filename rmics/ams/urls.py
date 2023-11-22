from .views import AddAsset
from . import views
from django.urls import path
from django.views.generic.edit import CreateView
from .models import Asset

#'asset_manufacturer', 'asset_model', 'asset_sub_model_01', 'asset_sub_model_02', 'asset_sub_model_03', 'asset_year', 'asset_month'

app_name = 'ams'


urlpatterns = [
    path('', views.Ams, name='ams_index'),
    path('asset-list/', views.AssetList, name='asset_list'),
    path('add-asset/', views.AddAsset.as_view(), name='add_asset'),
    path('<int:pk>/', views.AssetDetail.as_view(), name='asset_detail'),
    path('update-asset/<int:id>/', views.UpdateAsset, name='update_asset'),
    path('delete-asset/<int:id>/', views.DeleteAsset, name='delete_asset'),
    path('add-plant/', views.add_plant, name='add_plant'),
    path('plant-list/', views.plant_list, name='plant_list'),

]
