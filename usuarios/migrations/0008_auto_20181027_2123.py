# Generated by Django 2.0.7 on 2018-10-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20181027_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilsaude',
            name='sexo',
            field=models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'Feminino')], max_length=1, null=True, verbose_name='Sexo'),
        ),
    ]
