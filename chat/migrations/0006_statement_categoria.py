# Generated by Django 2.0.7 on 2018-08-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20180805_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='categoria',
            field=models.ManyToManyField(related_name='categorias', to='chat.Tag'),
        ),
    ]