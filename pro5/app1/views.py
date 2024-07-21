from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect 

from .forms import LaptopForm
from .models import Laptop
from django.contrib.auth.decorators import login_required

@login_required(login_url="/a2/login/")
def add_laptop(request):
    form=LaptopForm()
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/show/")
    return render(request,'app1/add.html',{'form':form})    
@login_required(login_url="/a2/login/")
def show_laptop(request):
    queryset=Laptop.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})


def updateview(request,pk):
    obj=Laptop.objects.get(id=pk)
    form=LaptopForm(instance=obj)
    if request.method=='POST':
        form=LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})  


def deleteview(request,x):
    obj = Laptop.objects.get(id=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})