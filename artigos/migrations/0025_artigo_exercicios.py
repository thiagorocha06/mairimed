# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_question_enunciado'),
        ('artigos', '0024_auto_20180203_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='exercicios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Exercícios'),
        ),
    ]
