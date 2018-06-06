# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_saude', '0003_auto_20180527_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='titulo_figura',
        ),
        migrations.AddField(
            model_name='materia',
            name='figura_maior',
            field=models.ImageField(blank=True, help_text='Corresponde à figura de destaque geral', null=True, upload_to='img/portal_saude'),
        ),
        migrations.AddField(
            model_name='materia',
            name='figura_menor',
            field=models.ImageField(blank=True, help_text='Corresponde à figura de destaque menor', null=True, upload_to='img/portal_saude'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='titulo_figura_texto',
            field=models.CharField(blank=True, help_text='Corresponde ao texto de destaque geral', max_length=200, null=True),
        ),
    ]