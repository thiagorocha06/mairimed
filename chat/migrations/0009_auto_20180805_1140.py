# Generated by Django 2.0.7 on 2018-08-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20180805_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statement',
            old_name='categoria',
            new_name='categorias',
        ),
    ]