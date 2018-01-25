# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercicios', '0003_remove_exercicio_data_de_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='data_de_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]