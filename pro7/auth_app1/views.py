from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def signup_view(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a2/login/')
    return render(request,'auth_app1/signup.html',{'form':form})   

def login_view(request):
    if request.method=='POST':
        u=request.POST.get("unm")
        p=request.POST.get("pwd")
        user=authenticate(username=u,password=p)
        if user != None:
            login(request,user)
            return redirect("/a1/show/")
    return render(request,'auth_app1/login.html',{})

def logout_view(request):
    logout(request)
    return redirect('/a2/login/')     



