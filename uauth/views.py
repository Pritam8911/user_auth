from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")
@csrf_exempt
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.error(request,"Username already Taken")
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.error(request,"Email already Taken")

            else:

                myuser=User.objects.create_user(username=username,email=email,password=password)
                myuser.save()
                messages.info(request,"Successfully Registered")
                return redirect('signin')

    return render(request,"signup.html")
@csrf_exempt
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if User is not None:
            login(request,user)
            username=user.username
            return render(request,'home.html',{'username':username})
        else:
            messages.error(request,"Invalid username/password")
            return redirect('home.html')


    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.error(request,"Logged out!")
    return render(request,'signup.html')

