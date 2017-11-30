# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# Manage your urls here.

app_name = 'wines'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main[/]?$', views.main, name='main'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^services.html$', views.service, name='service'),
    url(r'^add', views.add_wine, name='add_wine'),
    url(r'^wine/(?P<wine_id>[0-9]+)$', views.wine, name='wine'),
    url(r'^supplier/(?P<supplier_id>[0-9]+)/$', views.supplier, name='supplier'),
]
