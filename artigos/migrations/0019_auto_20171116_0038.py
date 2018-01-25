# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-16 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0018_auto_20171115_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='class_texto6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='class_top6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='epidemio_texto6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='epidemio_top6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]