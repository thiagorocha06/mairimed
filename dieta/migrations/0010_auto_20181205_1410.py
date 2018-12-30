# Generated by Django 2.0.7 on 2018-12-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0009_auto_20181205_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name': 'Desjejum',
                'verbose_name_plural': 'Desjejuns',
            },
        ),
        migrations.CreateModel(
            name='Lanche1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name': 'Lanche da manhã',
                'verbose_name_plural': 'Lanches da manhã',
            },
        ),
        migrations.RemoveField(
            model_name='refeicao',
            name='alimento',
        ),
        migrations.RemoveField(
            model_name='refeicao',
            name='dieta',
        ),
        migrations.DeleteModel(
            name='Refeicao',
        ),
    ]