# Generated by Django 2.0.7 on 2018-12-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0013_auto_20181211_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='porcao',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
