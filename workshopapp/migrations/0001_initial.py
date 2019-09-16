# Generated by Django 2.2.4 on 2019-08-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('course_durations', models.CharField(max_length=100)),
                ('course_fees', models.IntegerField(max_length=100)),
                ('course_start_date', models.DateField(max_length=100)),
                ('course_start_time', models.TimeField(max_length=100)),
                ('course_trainer_name', models.CharField(max_length=100)),
                ('course_trainer_exp', models.CharField(max_length=100)),
            ],
        ),
    ]
