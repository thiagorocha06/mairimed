# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0017_auto_20171111_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_texto6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='complicacoes_top6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]