# Generated by Django 2.0.7 on 2018-10-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_perfilsaude_meta_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilsaude',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]