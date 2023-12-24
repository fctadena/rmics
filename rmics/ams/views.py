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




def Ams(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/ams.html', context)

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


# class AssetDetail(DetailView):
#     model = Asset
#     template_name = 'ams/asset-detail.html'


class AssetDetail(DetailView):
    model = Asset
    template_name = 'ams/asset-detail.html'
    context_object_name = 'asset'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access related maintenance logs and pass them to the template
        context['related_maintenance_log'] = self.object.maintenance_logs_equipment.all()
        return context
    
    
    

#CRUD STARTS HERE
class AddAsset(CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'ams/add-asset.html'
    
    def get_success_url(self):
        messages.success(self.request, 'CREATED ASSET SUCCESSFULLY', extra_tags='success')
        return reverse_lazy('ams:asset_list')



def DeleteAsset(request,id):
    asset = Asset.objects.get(id=id)
    
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'DELETED ASSET SUCCESSFULLY', extra_tags='warning')
        return redirect('ams:asset_list')
    
    return render(request, 'ams/delete-asset.html', {'asset':asset})



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


def add_plant(request):
    # if request.method == "POST":
    #     form = PlantForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'ADDED PLANT SUCCESSFULLY', extra_tags='success')
    #         return redirect('ams:plant_list')
        
            
    # else:
    #     form = PlantForm()
    
    return render(request, 'ams/add-plant.html')


def plant_list(request):
    plant = PlantAssignment.objects.all()
    return render(request, 'ams/plant-list.html', {'plant':plant})



def delete_plant(request, id):
    plant = PlantAssignment.objects.get(id=id)
    
    if request.method == "POST":
        plant.delete()
        messages.success(request, 'SUCCESSFULLY DELETED PLANT', extra_tags="warning")
        return redirect('ams:plant_list')
    
    return render(request, 'ams/delete-plant.html', {'plant':plant})


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
        




# def edit_plant(request, id=id):
#     plant = PlantAssignment.objects.get(id=id)
#     if request.method == "POST":
#         form = PlantForm(request.POST, instance=plant)
#         if form.is_valid():
#             plant = form.save(commit=False)
#             plant.save()
            
            