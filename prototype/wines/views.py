# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Wine

# Create your views here.

def main(request):
    return render(request, 'wines/main.html', {});

def about(request):
    return render(request, 'wines/about.html', {});

def service(request):
    return render(request, 'wines/services.html', {});

def index(request):
    latest_wine_list = Wine.objects.order_by('-date')[:5]
    context = {
        'latest_wine_list': latest_wine_list,
    }
    return render(request, 'wines/index.html', context)

def wine(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    return render(request, 'wines/wine.html', {'wine': wine})

def supplier(request, supplier_id):
    return HttpResponse("You're looking at Supplier %s" % supplier_id)

def add_wine(request):
    if request.method == 'GET':
        return render(request, 'wines/add_wine.html', {})
    else:
        w = Wine(name = request.GET.get('name', None), wine_type = request.GET.get('wine_type', None), nation = request.GET.get('nation', None), district = request.GET.get('district', None), date = request.GET.get('date', None), shelf_life = request.GET.get('shelf_life', None), grape_type = request.GET.get('grape_type', None), alcohol = request.GET.get('alcohol', None), volume = request.GET.get('volume', None), supplier = request.GET.get('supplier', None))
        w.save()

