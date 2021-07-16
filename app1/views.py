from django.shortcuts import render , get_object_or_404
from .models import *

# Create your views here.

def index1(request):
    context = {'device' : 'divs' }
    return render(request , 'index.html',context)

def single_product(request , slug):
    device_detail = get_object_or_404(Device ,slug_dev=slug)
    context = {'device' : device_detail }
    return render(request , 'single-product.html',context)

def brand_devices(request ,brd):
    lista = Device.objects.filter(brand=brd)
    context = {'device' : lista }
    return render(request , 'pages/brand-devices.html',context)

def brands_list(request):
    context = {'brands' : Brand.objects.all() }
    return render(request , 'pages/brands.html',context)

def brand_spares(request):
    context = {'brands' : Brand.objects.all() }
    return render(request , 'pages/brand-spares.html',context)

def brand_accessories(request):
    context = {'brands' : Brand.objects.all() }
    return render(request , 'pages/brand-accessories.html',context)