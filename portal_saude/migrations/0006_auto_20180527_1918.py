# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_saude', '0005_auto_20180527_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='destaque_geral',
        ),
        migrations.AddField(
            model_name='materia',
            name='destaque_geral1',
            field=models.BooleanField(default=False, help_text='Se marcado, a materia sera mostrado na página destaque geral como número 1', verbose_name='Materia destaque geral 1'),
        ),
        migrations.AddField(
            model_name='materia',
            name='destaque_geral2',
            field=models.BooleanField(default=False, help_text='Se marcado, a materia sera mostrado na página destaque geral como número 2', verbose_name='Materia destaque geral 2'),
        ),
        migrations.AddField(
            model_name='materia',
            name='destaque_geral3',
            field=models.BooleanField(default=False, help_text='Se marcado, a materia sera mostrado na página destaque geral como número 3', verbose_name='Materia destaque geral 3'),
        ),
    ]