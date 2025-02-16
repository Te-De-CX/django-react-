from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")

def signIn(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    passwordagain = request.POST["passwordAgain"]
    
    if request.method == "POST":
        if password == passwordagain:
            if User.objects.filter (email=email).exists():
                messages.info(request,"Email ALready exists")
                return redirect("signIn")
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect("signIn")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"Passwords doesnt match")
            return redirect("signIn")
    else:
        return render(request, "signIn.html")

# def login(request)