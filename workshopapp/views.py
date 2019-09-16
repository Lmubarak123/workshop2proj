from django.shortcuts import render
from .models import ServicesData,FeedbackData,Enquairymodel
from.forms import Feedbackform,Equairyform
from django.http import HttpResponse
import datetime as dt
date1=dt.datetime.now()
# Create your views here.
def home_view(request):
    return render(request,'home.html')


def services_view(request):
    ser=ServicesData.objects.all()
    return render(request,'services.html',{'ser':ser})


def equairy_view(request):
    if request.method=='POST':
        eform=Equairyform(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            courses=eform.cleaned_data.get('courses')
            shifts=eform.cleaned_data.get('shifts')
            start_date=eform.cleaned_data.get('start_date')

            data=Enquairymodel(
                name=name,
                mobile=mobile,
                email=email,
                course=courses,
                shifts=shifts,
                start_date=start_date
            )
            data.save()
            return render(request,'contact.html',{'data':data})
        else:
            return HttpResponse("User Entered Invalid Data")

    else:
        eform=Equairyform()


    return render(request,'contact.html',{'eform':eform})


def gallery_view(request):
    return render(request,'gallery.html')


def feedback_view(request):
    if request.method=='POST':
        ffrom=Feedbackform(request.POST)
        if ffrom.is_valid():

            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(name=name,rating=rating,feedback=feedback,date=date1)
            data.save()
            ffrom=Feedbackform()
            fdata=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':ffrom,'fdata':fdata})
        else:
            return HttpResponse("Invalid User Data")
    else:
        ffrom=Feedbackform()
        fdata=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':ffrom,'fdata':fdata})


