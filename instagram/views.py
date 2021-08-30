from django.contrib.auth.signals import user_logged_in
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')


def chat(request):
    return render(request, 'chat.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        user = User(name=name, email=email,
                    username=username, password=password)
        user.save()
        print("User Save in Database. User: {user}")
        return redirect(request, 'login.html')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect(request, 'home')
    else:
        if request.method == "POST":
            loginemail = request.POST['loginemail']
            loginpassword = request.POST['loginpassword']
            print(loginemail, loginpassword)
            user = authenticate(username=loginemail, password=loginpassword)
            print(user)
            if user is not None:
                login(user)
                return redirect('home')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def handeleLogout(request):
    logout(request)
    return redirect(request, 'login.html')
