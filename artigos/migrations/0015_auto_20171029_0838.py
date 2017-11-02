# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-29 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0014_artigo_exames_img3'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='profilaxia_texto5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='profilaxia_texto6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='profilaxia_top5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='profilaxia_top6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
