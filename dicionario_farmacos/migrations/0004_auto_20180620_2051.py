# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_farmacos', '0003_auto_20180620_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmaco',
            name='contraindicacoes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='farmacocinetica',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='farmacodinamica',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='gravidez',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='indicacoes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='interacoes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='introducao',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='posologia',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='precaucoes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='reacoes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
