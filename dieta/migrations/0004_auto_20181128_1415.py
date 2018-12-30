# Generated by Django 2.0.7 on 2018-11-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0003_auto_20181103_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieta',
            name='user',
        ),
        migrations.AddField(
            model_name='dieta',
            name='nome_dieta',
            field=models.CharField(default='dieta', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_dom',
            field=models.ManyToManyField(blank=True, related_name='almoco_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_qua',
            field=models.ManyToManyField(blank=True, related_name='almoco_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_qui',
            field=models.ManyToManyField(blank=True, related_name='almoco_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_sab',
            field=models.ManyToManyField(blank=True, related_name='almoco_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_seg',
            field=models.ManyToManyField(blank=True, related_name='almoco_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_sex',
            field=models.ManyToManyField(blank=True, related_name='almoco_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='almoco_ter',
            field=models.ManyToManyField(blank=True, related_name='almoco_ter', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_dom',
            field=models.ManyToManyField(blank=True, related_name='desjejum_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_qua',
            field=models.ManyToManyField(blank=True, related_name='desjejum_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_qui',
            field=models.ManyToManyField(blank=True, related_name='desjejum_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_sab',
            field=models.ManyToManyField(blank=True, related_name='desjejum_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_seg',
            field=models.ManyToManyField(blank=True, related_name='desjejum_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_sex',
            field=models.ManyToManyField(blank=True, related_name='desjejum_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='desjejum_ter',
            field=models.ManyToManyField(blank=True, related_name='desjejum_ter', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_dom',
            field=models.ManyToManyField(blank=True, related_name='jantar_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_qua',
            field=models.ManyToManyField(blank=True, related_name='jantar_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_qui',
            field=models.ManyToManyField(blank=True, related_name='jantar_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_sab',
            field=models.ManyToManyField(blank=True, related_name='jantar_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_seg',
            field=models.ManyToManyField(blank=True, related_name='jantar_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_sex',
            field=models.ManyToManyField(blank=True, related_name='jantar_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='jantar_ter',
            field=models.ManyToManyField(blank=True, related_name='jantar_ter', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_dom',
            field=models.ManyToManyField(blank=True, related_name='lanche1_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_qua',
            field=models.ManyToManyField(blank=True, related_name='lanche1_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_qui',
            field=models.ManyToManyField(blank=True, related_name='lanche1_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_sab',
            field=models.ManyToManyField(blank=True, related_name='lanche1_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_seg',
            field=models.ManyToManyField(blank=True, related_name='lanche1_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_sex',
            field=models.ManyToManyField(blank=True, related_name='lanche1_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche1_ter',
            field=models.ManyToManyField(blank=True, related_name='lanche1_ter', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_dom',
            field=models.ManyToManyField(blank=True, related_name='lanche2_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_qua',
            field=models.ManyToManyField(blank=True, related_name='lanche2_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_qui',
            field=models.ManyToManyField(blank=True, related_name='lanche2_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_sab',
            field=models.ManyToManyField(blank=True, related_name='lanche2_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_seg',
            field=models.ManyToManyField(blank=True, related_name='lanche2_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_sex',
            field=models.ManyToManyField(blank=True, related_name='lanche2_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche2_ter',
            field=models.ManyToManyField(blank=True, related_name='lanche2_ter', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_dom',
            field=models.ManyToManyField(blank=True, related_name='lanche3_dom', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_qua',
            field=models.ManyToManyField(blank=True, related_name='lanche3_qua', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_qui',
            field=models.ManyToManyField(blank=True, related_name='lanche3_qui', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_sab',
            field=models.ManyToManyField(blank=True, related_name='lanche3_sab', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_seg',
            field=models.ManyToManyField(blank=True, related_name='lanche3_seg', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_sex',
            field=models.ManyToManyField(blank=True, related_name='lanche3_sex', to='dieta.Alimento'),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='lanche3_ter',
            field=models.ManyToManyField(blank=True, related_name='lanche3_ter', to='dieta.Alimento'),
        ),
    ]