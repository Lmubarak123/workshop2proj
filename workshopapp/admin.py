from django.contrib import admin
from.models import ServicesData ,Enquairymodel
# Register your models here.
class AdminServicesData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_durations',
                    'course_fees',
                    'course_start_date',
                    'course_start_time',
                    'course_trainer_name',
                    'course_trainer_exp']
admin.site.register(ServicesData,AdminServicesData)
class AdmincontactData(admin.ModelAdmin):
    list_display = [
        'name','mobile','email','gender','course','shifts','start_date'
    ]
admin.site.register(Enquairymodel,AdmincontactData)
