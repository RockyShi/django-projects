# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Wine

# Create your views here.

def index(request):
    latest_wine_list = Wine.objects.order_by('-date')[:5]
    template = loader.get_template('wines/index.html')
    context = {
        'latest_wine_list': latest_wine_list,
    }
    return HttpResponse(template.render(context, request))

def wine(request, wine_id):
    return HttpResponse("You're looking at Wine %s" % wine_id)

def supplier(request, supplier_id):
    return HttpResponse("You're looking at Supplier %s" % supplier_id)
