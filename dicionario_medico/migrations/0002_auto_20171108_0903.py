# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_medico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termo',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='termo',
            name='tipo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
