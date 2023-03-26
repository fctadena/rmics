from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Asset
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import AssetForm
from django.http import HttpResponse


def Ams(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/ams.html', context)

def AssetList(request):
    asset_list = Asset.objects.all()
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'ams/asset-list.html', context)


def AssetDetail(request):
    html = "<html><body><h1>AssetDetail</h1></body></html>"
    return HttpResponse(html)

def UpdateAsset(request):
    html = "<html><body><h1>UpdateAsset</h1></body></html>"
    return HttpResponse(html)



def AddAsset(request):
    form = AssetForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('ams:add_asset')
    
    return render(request, 'ams/add-asset.html', {'form': form })
    
    



def DeleteAsset(request):
    html = "<html><body><h1>DeleteAsset</h1></body></html>"
    return HttpResponse(html)