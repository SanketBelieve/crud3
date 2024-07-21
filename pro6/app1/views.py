from django.shortcuts import render,redirect
from .forms import MobileForm
from .models import Mobile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/a2/login/')
def add_mobile(request):
    form=MobileForm()
    if request.method=='POST':
        form=MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/show/")
    return render(request,'app1/add.html',{'form':form})   
@login_required(login_url='/a2/login/')
def show_mobile(request):
    queryset=Mobile.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})      


def update_mobile(request,pk):
    obj=Mobile.objects.get(mid=pk)
    form=MobileForm(instance=obj)
    if request.method=='POST':
        form=MobileForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})    
   
   
def delete_mobile(request,x):
    obj=Mobile.objects.get(mid=x)   
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})