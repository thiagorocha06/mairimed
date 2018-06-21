# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dicionario_doencas', '0007_auto_20180621_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='doenca',
            name='data_de_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='doenca',
            name='data_de_publicacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
