# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_farmacos', '0007_auto_20180621_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmaco',
            name='interacoes',
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='contraindicacoes',
            field=models.TextField(blank=True, help_text='contraindicacoes', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='farmacocinetica',
            field=models.TextField(blank=True, help_text='farmacocinetica', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='farmacodinamica',
            field=models.TextField(blank=True, help_text='farmacodinamica', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='gravidez',
            field=models.TextField(blank=True, help_text='gravidez', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='indicacoes',
            field=models.TextField(blank=True, help_text='indicacoes', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='introducao',
            field=models.TextField(blank=True, help_text='introducao', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='lactacao',
            field=models.TextField(blank=True, help_text='lactacao', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='pediatria',
            field=models.TextField(blank=True, help_text='pediatria', null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='posologia',
            field=models.TextField(blank=True, help_text='posologia', null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='precaucoes',
            field=models.TextField(blank=True, help_text='precaucoes', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='reacoes',
            field=models.TextField(blank=True, help_text='reacoes', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='farmaco',
            name='texto',
            field=models.TextField(blank=True, help_text='texto acessorio', null=True),
        ),
    ]