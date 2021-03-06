# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Instituicao')),
            ],
            options={
                'verbose_name_plural': 'Instituições',
                'verbose_name': 'Instituição',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('link', models.CharField(help_text='link', max_length=200)),
            ],
        ),
    ]
