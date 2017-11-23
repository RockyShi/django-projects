# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Wine(models.Model):
    name = models.CharField(max_length=200)
    wine_type = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    date = models.DateTimeField('date bottled')
    shelf_life = models.IntegerField()
    grape_type = models.CharField(max_length=50)
    alcohol = models.FloatField()
    volume = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name
    def is_overdue(self):
        return date.today().year - self.date.year > self.shelf_life


    
