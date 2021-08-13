from django.shortcuts import render
from .models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


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

    return render(request, 'signup.html')
