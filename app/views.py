from django.shortcuts import render
from .forms import AppointmentForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method=="POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('/')
    else:
        form=AppointmentForm
    return render(request,'home.html',{'form':form})

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def department(request):
    return render(request,'department.html')

def doctor(request):
    return render(request,'doctor.html')

def contact(request):
    return render(request,'contact.html')