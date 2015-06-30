from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from login.models import HelpUser

def index(request):
    return render(request, 'login/login.html')

@csrf_exempt
def showregister(request):
    return render(request, 'login/register.html')

@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, "/helpstl/")
    else:
        return render(request, "/")


def register(request):
    uname = request.POST.get("username")
    password = request.POST.get("password")
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    zip = request.POST.get("zip")

    user = HelpUser.objects.create(user)