from django.shortcuts import render
from django.http import HttpResponse
from Myapp.models import Dept

# Create your views here.
def Hello(request):
    return HttpResponse("hello you are good to go")

def addDept(request):
    return render(request,"addDept.html",{})

def saveDept(request):
    Did = request.POST["Did"]
    Dname = request.POST["Dname"]
    Dlocation = request.POST["Dlocation"]

    d1 = Dept(Did,Dname,Dlocation)
    d1.save()
    return HttpResponse("data added successfully")
