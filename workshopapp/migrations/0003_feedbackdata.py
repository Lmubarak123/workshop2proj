# Generated by Django 2.2.4 on 2019-08-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0002_auto_20190822_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
