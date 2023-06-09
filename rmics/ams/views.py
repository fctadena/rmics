from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Asset
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import AssetForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages





def Ams(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/asset-list.html', context)

def AssetList(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/asset-list.html', context)


class AssetDetail(DetailView):
    model = Asset
    template_name = 'ams/asset-detail.html'



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
    return render(request, 'ams/add-asset.html', {'form': form, 'asset': asset})
