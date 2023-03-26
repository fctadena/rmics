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
    path('add-asset/', views.AddAsset, name='add_asset'),
    path('asset-detail/', views.AssetDetail, name='asset_detail'),
    path('update-asset/', views.UpdateAsset, name='update_asset'),
    path('delete-asset/', views.DeleteAsset, name='delete_asset'),
]
