# Generated by Django 2.0.7 on 2018-12-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0012_auto_20181211_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='porcao',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='alimento',
            name='unidade',
            field=models.CharField(default='g', max_length=30),
            preserve_default=False,
        ),
    ]
