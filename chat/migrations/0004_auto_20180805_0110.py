# Generated by Django 2.0.7 on 2018-08-05 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20180729_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='text',
        ),
    ]
