# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-22 18:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(default='', max_length=50)),
                ('ultimo_nome', models.CharField(default='', max_length=50)),
                ('instituicao', models.CharField(default='', max_length=30)),
                ('semestre', models.CharField(default='', max_length=10)),
                ('artigos_favoritos', models.ManyToManyField(related_name='favorited_by', to='artigos.Artigo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
