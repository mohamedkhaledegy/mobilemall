from django.shortcuts import render
from . import models

# Create your views here.

def index1(request):
    context = {'device' : 'divs' }
    return render(request , 'index.html',context)

def single_product(request):
    context = {'device' : 'divs' }
    return render(request , 'single-product.html',context)