# Generated by Django 2.0.7 on 2018-12-13 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0017_auto_20181211_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='DomDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='DomJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='DomLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuaAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuaDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuaJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuaLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuiAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuiDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuiJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='QuiLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SabAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SabDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SabJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SabLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SegAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SegDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Desjejuns',
                'verbose_name': 'Desjejum',
            },
        ),
        migrations.CreateModel(
            name='SegJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SegLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SexAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SexDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SexJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='SexLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='TerAlmoco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='TerDesjejum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='TerJantar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.CreateModel(
            name='TerLanches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True)),
                ('alimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.Alimento')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.Dieta')),
            ],
            options={
                'verbose_name_plural': 'Almoços',
                'verbose_name': 'Almoço',
            },
        ),
        migrations.RemoveField(
            model_name='almoco',
            name='alimento',
        ),
        migrations.RemoveField(
            model_name='almoco',
            name='dieta',
        ),
        migrations.RemoveField(
            model_name='desjejum',
            name='alimento',
        ),
        migrations.RemoveField(
            model_name='desjejum',
            name='dieta',
        ),
        migrations.DeleteModel(
            name='Almoco',
        ),
        migrations.DeleteModel(
            name='Desjejum',
        ),
    ]