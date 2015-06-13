__author__ = 'James'
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def helpstl(request):
    return render(request, "helpstl/helpstl.html")