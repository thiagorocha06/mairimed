# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario_termos', '0004_termo_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termo',
            name='definicao',
            field=models.TextField(blank=True, help_text='definicao', null=True),
        ),
        migrations.AlterField(
            model_name='termo',
            name='origem',
            field=models.TextField(blank=True, help_text='origem', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='termo',
            name='texto',
            field=models.TextField(blank=True, help_text='texto acessorio', null=True),
        ),
        migrations.AlterField(
            model_name='termo',
            name='tipo',
            field=models.CharField(blank=True, help_text='tipo', max_length=200, null=True),
        ),
    ]