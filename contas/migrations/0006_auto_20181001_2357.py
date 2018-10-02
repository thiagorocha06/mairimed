# Generated by Django 2.0.7 on 2018-10-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_auto_20181001_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilestudante',
            name='faculdade',
            field=models.CharField(choices=[('1', 'ESCS'), ('2', 'UNB'), ('3', 'UCB'), ('4', 'UNICEUB'), ('5', 'FACIPLAC')], default='', max_length=1, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='perfilestudante',
            name='primeiro_nome',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='perfilestudante',
            name='ultimo_nome',
            field=models.TextField(default='', max_length=30),
        ),
    ]
