
from django.shortcuts import render,redirect 

from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required(login_url="/a2/login/")
def add_employee(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/show/")
    return render(request,'app1/add.html',{'form':form})    
@login_required(login_url="/a2/login/")
def show_employee(request):
    queryset=Employee.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})


def updateview(request,pk):
    obj=Employee.objects.get(eid=pk)
    form=EmployeeForm(instance=obj)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})  


def deleteview(request,x):
    obj = Employee.objects.get(eid=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})