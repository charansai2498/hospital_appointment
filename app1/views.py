from django.shortcuts import render,redirect
from app1.forms import *
# Create your views here.
def doctoradd(request):
    msg=''
    if request.method=='POST':
        d=DoctorForm(request.POST)
        if d.is_valid():
            d.save()
            msg='Doctor Details Added'            
    form=DoctorForm()
    return render(request,'adddoctor.html',{'form':form,'msg':msg})
def listdoctors(request):
    qs=DoctorForm.objects.all()
    return render(request,'listdoctor_temp.html',{'qs':qs})
def home(request):
    return render(request,'base.html')    
    