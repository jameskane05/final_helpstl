__author__ = 'James'
from django.shortcuts import render, redirect
from helpstl.models import HelpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def helpstl(request):
    helpreqs = HelpRequest.objects.all()
    return render(request, "helpstl/helpstl.html", {'helpreqs': helpreqs})

def request(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        helpreq = HelpRequest.objects.get(id=id)
        return render(request, "helpstl/request.html", {'helpreq': helpreq})

def map(request):
    return render(request, "helpstl/map.html")