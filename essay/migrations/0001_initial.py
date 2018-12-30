# Generated by Django 2.0.7 on 2018-10-15 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
                'verbose_name_plural': 'Essay style questions',
                'verbose_name': 'Essay style question',
            },
            bases=('quiz.question',),
        ),
    ]
