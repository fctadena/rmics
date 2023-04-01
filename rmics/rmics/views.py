from . import views
from django.http import HttpResponse
from django.shortcuts import render, redirect



def Index(request):
 
    return render(request, 'rmics/base.html')