# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# Manage your urls here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine, name='wine'),
    url(r'^supplier/(?P<supplier_id>[0-9]+)/$', views.supplier, name='supplier'),
]
