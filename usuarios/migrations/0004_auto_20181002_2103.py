# Generated by Django 2.0.7 on 2018-10-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20181002_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilestudante',
            name='primeiro_nome',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='perfilestudante',
            name='ultimo_nome',
            field=models.CharField(default='', max_length=30),
        ),
    ]
