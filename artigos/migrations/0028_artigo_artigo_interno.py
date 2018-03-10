# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0027_auto_20180204_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='artigo_interno',
            field=models.BooleanField(default=False, help_text='Se marcado, o artigo sera mostrado apenas para internos conectados', verbose_name='Artigo para Internos'),
        ),
    ]