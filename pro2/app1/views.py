from django.shortcuts import render,redirect 

from .forms import BankForm 
from .models import Bank
from django.contrib.auth.decorators import login_required

@login_required(login_url="/a2/login/")
def add_person(request):
    form=BankForm()
    if request.method=='POST':
        form=BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/show/")
    return render(request,'app1/add.html',{'form':form})    
@login_required(login_url="/a2/login/")
def show_person(request):
    queryset=Bank.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})


def updateview(request,pk):
    obj=Bank.objects.get(bid=pk)
    form=BankForm(instance=obj)
    if request.method=='POST':
        form=BankForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})  


def deleteview(request,x):
    obj = Bank.objects.get(bid=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})