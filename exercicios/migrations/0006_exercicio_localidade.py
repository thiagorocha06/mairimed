# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercicios', '0005_exercicio_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='localidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
