from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Registeration
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request,'home.html')

def Registration(request):
    if request.method=="POST":
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone = request.POST["phone"]
        password = request.POST["Password"]
        gender = request.POST["Gender"]
        usr = User.objects.create_user(name,email,password)
        usr.save()
        record = Registeration(Name=name,Email=email,Mobile=phone,Password=password,Gender=gender)
        record.save()
        return redirect(Home)
    return render(request,'Registration.html')


def Login(request):
    if request.method=="POST":
        loginname = request.POST["name"]  
        loginemail = request.POST['email']
        loginpassword = request.POST["Password"]  
        user = authenticate(username=loginname, email=loginemail, password=loginpassword)
        if user is not None:
            login(request,user)
            if request.GET.get('next', None):
                return redirect(request.GET['next']) 
            return redirect(analyser)
            
        else:
            return redirect(Home)         
    return render(request,'login.html')


@login_required(login_url='/login/')
def analyser(request):
    return render(request,'main.html')


@login_required()
def signout(request):
    logout(request)
    return redirect(Home)
    

def FAQ(request):
    return render(request,'FAQ.html')