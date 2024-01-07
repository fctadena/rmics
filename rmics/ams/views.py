from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Asset, PlantAssignment
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import AssetForm, PlantForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated_logic, allowed_groups
from django.utils.decorators import method_decorator



@unauthenticated_logic
def AssetList(request):
    asset_list = Asset.objects.all()
    search_asset = request.GET.get('search_asset')
    
    if search_asset is not None:
        asset_list = asset_list.filter(
            Q(asset_model__icontains=search_asset) |  # Search asset_model field
            Q(asset_manufacturer__icontains=search_asset) |  # Search asset_manufacturer field
            Q(asset_type__icontains=search_asset) |  # Search asset_type field
            Q(asset_sub_type__icontains=search_asset) |  # Search asset_sub_type field
            Q(asset_drive_details__icontains=search_asset) |   # Search asset_drive_details field
            Q(asset_rated_capacity__icontains=search_asset)    # Search asset_rated_capacity field
        )
        
    
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/asset-list.html', context)



@method_decorator(unauthenticated_logic, name='dispatch')
class AssetDetail(DetailView):
    model = Asset
    template_name = 'ams/asset-detail.html'
    context_object_name = 'asset'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access related maintenance logs and pass them to the template
        context['related_maintenance_log'] = self.object.maintenance_logs_equipment.all()
        return context

@method_decorator(unauthenticated_logic, name='dispatch')
@method_decorator(allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management']), name='dispatch')
class AddAsset(CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'ams/add-asset.html'
    
    def get_success_url(self):
        messages.success(self.request, 'CREATED ASSET SUCCESSFULLY', extra_tags='success')
        return reverse_lazy('ams:asset_list')


@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management'])
def DeleteAsset(request,id):
    asset = Asset.objects.get(id=id)
    
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'DELETED ASSET SUCCESSFULLY', extra_tags='warning')
        return redirect('ams:asset_list')
    
    return render(request, 'ams/delete-asset.html', {'asset':asset})


@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Site Management'])
def UpdateAsset(request,id):
    asset = Asset.objects.get(id=id)
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES, instance=asset)
        if form.is_valid():
            asset = form.save(commit=False)
            # Handle file upload
            if 'asset_image_primary' in request.FILES:
                asset.asset_image_primary = request.FILES['asset_image_primary']
            asset.save()
            messages.success(request, 'UPDATED ASSET SUCCESSFULLY', extra_tags='info')
            return redirect('ams:asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'ams/update-asset.html', {'form': form, 'asset': asset})

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def add_plant(request):

    return render(request, 'ams/add-plant.html')

@unauthenticated_logic
def plant_list(request):
    plant = PlantAssignment.objects.all()
    return render(request, 'ams/plant-list.html', {'plant':plant})


@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def delete_plant(request, id):
    plant = PlantAssignment.objects.get(id=id)
    
    if request.method == "POST":
        plant.delete()
        messages.success(request, 'SUCCESSFULLY DELETED PLANT', extra_tags="warning")
        return redirect('ams:plant_list')
    
    return render(request, 'ams/delete-plant.html', {'plant':plant})

@unauthenticated_logic
@allowed_groups(allowed_roles=['Operations Analyst Super', 'Operations Analyst'])
def update_plant(request, id):
    plant = PlantAssignment.objects.get(id=id)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.save()
            messages.success(request, 'SUCCESSFULLY UPDATED PLANT', extra_tags='info')
            return redirect('ams:plant_list')
    
    else:
        form = PlantForm(instance=plant)
    return render(request, 'ams/update-plant.html', {'form':form, 'plant':plant})            



@unauthenticated_logic
def Ams(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/ams.html', context)