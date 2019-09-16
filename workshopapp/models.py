from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_durations=models.CharField(max_length=100)
    course_fees=models.IntegerField()
    course_start_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.CharField(max_length=100)
class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField()
    feedback=models.CharField(max_length=500)

class Enquairymodel(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=10)

    COURSE_CHOICES=(
        ('PY','python'),
        ('DJ','django'),
        ('RA','restapi'),
        ('FL','flask'),
        ('UI','ui')
    )

    course=MultiSelectField(choices=COURSE_CHOICES)

    SHIFTS_CHOICES=(
        ('Morning','Morning shift'),
         ('Afternoon','Afternoon shift'),
         ('Evening','Evening shift'),
         ('Night','Night shift')
    )
    shifts = MultiSelectField(choices=SHIFTS_CHOICES)
    start_date=models.DateTimeField()


