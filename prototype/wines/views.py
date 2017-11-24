# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Wine

# Create your views here.

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
