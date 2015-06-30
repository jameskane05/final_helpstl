from django.shortcuts import render, redirect
from django.db import models
from datetime import datetime
from helpstl.models import HelpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def subform(request):
    return render(request, "submit/submit.html")

@csrf_exempt
def submit(request):

    if request.method == "POST":

        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        zip = request.POST.get('zip', '')
        headline = request.POST.get('headline', '')
        category = request.POST.get('category','')
        completed = request.POST.get('completed' '')
        geninfo = request.POST.get('geninfo', '')

        helpreq = HelpRequest.objects.create(first_name=fname, last_name=lname, email=email, phone=phone, zip=zip, headline=headline, category=category, completed=False, geninfo=geninfo)
        helpreq.save()

        return redirect("../helpstl/request.html?id=" + str(helpreq.id))