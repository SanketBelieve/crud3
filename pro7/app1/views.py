from django.shortcuts import render,redirect
from .forms import FootballForm
from .models import Football 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/a2/login/')
def add_view(request):
    form=FootballForm()
    if request.method=='POST':
        form=FootballForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/a1/show/')
    return render(request,'app1/add.html',{'form':form})    

@login_required(login_url='/a2/login/')
def show_view(request):
    queryset=Football.objects.all()
    
    return render(request,'app1/show.html',{'queryset':queryset})

def update_view(request,pk):
    obj=Football.objects.get(cid=pk)
    form=FootballForm(instance=obj)
    if request.method=='POST':
        form=FootballForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
    return render(request,'app1/add.html',{'form':form})    
    

def delete_view(request,x):
    obj=Football.objects.get(cid=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1.html/delete.html',{'obj':obj})

