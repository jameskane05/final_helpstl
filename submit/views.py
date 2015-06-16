from django.shortcuts import render, redirect
from django.db import models
from datetime import datetime
from helpstl.models import HelpReq
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def subform(request):
    return render(request, "submit/submit.html")


def submit(request):

    if request.method == "POST":

        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        dob = request.POST.get('dob', '')
        headline = request.POST.get('headline', '')
        date = models.DateField(default=datetime.now)
        completed = request.POST.get('completed' '')
        info = request.POST.get('info', '')

        helpreq = HelpReq.objects.create(fname=fname, lname=lname, email=email, phone=phone, dob=dob, headline=headline, date=date, completed=False, info=info)

        return JsonResponse({'id': helpreq.id}), render(request, "helpstl/request.html")
