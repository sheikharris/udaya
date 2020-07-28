from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from .models import airports_city,airport_img,airport_fact
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request,'home.html')

def port(request):

    return render(request,'airportlist.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('port')
        else:
            messages.info(request,"Username or Password is wrong")
            return redirect("login")

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']

        first=request.POST['first']
        last=request.POST['last']
        password1=request.POST['password1']
        email=request.POST['email']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email-id is already exists.")
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first,last_name=last,username=username,email=email,password=password1)
                user.save();
                return render(request,'login.html')



        else:
            messages.info(request,"password are not same")
            return redirect('signup')






    else:
      return render(request,'signup.html')


def airtel(request):
    return render(request,'airtel.html')

def emaildone(request):

    return render(request,'airportlist1.html')
