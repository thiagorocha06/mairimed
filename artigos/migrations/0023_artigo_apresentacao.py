# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0022_auto_20180111_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='apresentacao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]