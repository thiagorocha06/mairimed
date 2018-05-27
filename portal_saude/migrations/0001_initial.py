# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(blank=True, max_length=250, null=True, verbose_name='Assunto')),
            ],
            options={
                'verbose_name_plural': 'Assuntos',
                'verbose_name': 'Assunto',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_de_publicacao', models.DateTimeField(blank=True, null=True)),
                ('destaque_geral', models.BooleanField(default=False, help_text='Se marcado, a materia sera mostrado na página destaque geral', verbose_name='Materia destaque geral')),
                ('destaque_semana', models.BooleanField(default=False, help_text='Se marcado, o materia sera mostrado na página destaque da semana', verbose_name='Materia destaque da semana')),
                ('titulo', models.CharField(max_length=200)),
                ('titulo_figura', models.ImageField(blank=True, null=True, upload_to='img/portal_saude')),
                ('titulo_figura_texto', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.SlugField(help_text='a user friendly url', max_length=60, null=True, verbose_name='user friendly url')),
                ('top1', models.CharField(blank=True, max_length=200, null=True)),
                ('texto1', models.TextField(blank=True, null=True)),
                ('figura1', models.ImageField(blank=True, null=True, upload_to='img/portal_saude')),
                ('figura1_texto', models.CharField(blank=True, max_length=200, null=True)),
                ('assunto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal_saude.Assunto', verbose_name='Assunto')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
