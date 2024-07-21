from django.shortcuts import render,redirect
from .forms import OrderForm 
from .models import Order
# Create your views here.
def addview(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
    return render(request,'app1/add.html',{'form':form})   

def updateview(request,pk):
    obj=Order.objects.get(id=pk)
    form=OrderForm(instance=obj)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
    
    return render(request,'app1/add.html',{'form':form})

def showview(request):
    query=Order.objects.all()
    return render(request,'app1/show.html',{'objects':query})

def deleteview(request,x):
    obj=Order.objects.get(id=x)
    if request.method=='POST':
        obj.delete()
    return render(request,'app1/delete.html',{})    
    