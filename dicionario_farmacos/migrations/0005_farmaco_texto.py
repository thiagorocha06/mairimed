# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_farmacos', '0004_auto_20180620_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmaco',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
