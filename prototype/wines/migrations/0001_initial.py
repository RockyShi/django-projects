# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('addr', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('wine_type', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name='date bottled')),
                ('grape_type', models.CharField(max_length=50)),
                ('alcohol', models.FloatField()),
                ('volume', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wines.Supplier')),
            ],
        ),
    ]