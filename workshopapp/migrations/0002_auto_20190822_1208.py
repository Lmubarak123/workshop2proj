# Generated by Django 2.2.4 on 2019-08-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesdata',
            name='course_fees',
            field=models.IntegerField(),
        ),
    ]
