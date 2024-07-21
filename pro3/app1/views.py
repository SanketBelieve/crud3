from django.shortcuts import render,redirect
from .forms import StudentForm 
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/a2/login/')
def add_student(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/show.html/')
    return render(request,'app1/add.html',{'form':form})  

      
@login_required(login_url='/a2/login/')
def show_student(request):
    queryset=Student.objects.all()
    return render(request,'app1/show.html',{'objects':queryset})

def update_student(request,pk):
    obj=Student.objects.get(sid=pk)
    form=StudentForm(instance=obj)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/show/')
        
    return render(request,'app1/add.html',{'form':form})  
    

def deleteview(request,x):
    obj = Student.objects.get(sid=x)
    if request.method=='POST':
        obj.delete()
        return redirect('/a1/show/')
    return render(request,'app1/delete.html',{'obj':obj})  



  