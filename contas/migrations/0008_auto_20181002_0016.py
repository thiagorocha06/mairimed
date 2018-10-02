# Generated by Django 2.0.7 on 2018-10-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_remove_perfilestudante_faculdade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilestudante',
            old_name='user',
            new_name='estudante',
        ),
        migrations.AddField(
            model_name='perfilestudante',
            name='faculdade',
            field=models.CharField(choices=[('1', 'ESCS'), ('2', 'UNB'), ('3', 'UCB'), ('4', 'UNICEUB'), ('5', 'FACIPLAC')], default='ESCS', max_length=1, verbose_name='Instituição'),
        ),
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
