from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PlayerForm
from .models import Player
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/a2/login/")
def add_player(request):
    form=PlayerForm()
    if request.method=='POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/a1/show/")  
    return render(request,'app1/add.html',{'form':form})

@login_required(login_url="/a2/login/")
def show_player(request):
    queryset=Player.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})

def updateview(request,pk):
    obj=Player.objects.get(pid=pk)
    form=PlayerForm(instance=obj)
    if request.method=='POST':
        form=PlayerForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})  

def deleteview(request,x):
    obj = Player.objects.get(pid=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})