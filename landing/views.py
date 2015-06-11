from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def login(request):

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'helpstl/helpstl.html')
        else:
            return render(request, 'landing/login.html')


def register(request):
    if request.method == "POST":
        # Get POST params from request
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')

        if not username or not password or not confirm:
            return render(request, 'landing/login.html')
        elif password != confirm:
            return render(request, 'landing/login.html')

        user = User.objects.create_user(username, password=password)
        login(request, user)

        return render(request, "landing/landing.html")
