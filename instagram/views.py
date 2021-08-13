from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    # if request.method == "POST":
    #     email = request.POST.get('email',)
    #     name = request.POST.get('name', '')
    #     username = request.POST.get('username', '')
    #     password = request.POST.get('password', '')
    # print(f"Email: {email}Name: {name}Username: {username}Password: {password}")

    return render(request, 'signup.html')
