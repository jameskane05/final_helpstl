from django.shortcuts import render, redirect

def submit(request):
    return render(request, "submit/submit.html")