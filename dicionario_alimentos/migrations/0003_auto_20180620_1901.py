# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_alimentos', '0002_alimento_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='nome',
            field=models.CharField(default='nulo', max_length=200),
            preserve_default=False,
        ),
    ]
