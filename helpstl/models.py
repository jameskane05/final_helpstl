from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# # Store additional information related to a user
class HelpReq(models.Model):
    fname = models.CharField(max_length=25, default="")
    lname = models.CharField(max_length=25, default="")
    email = models.CharField(max_length=254, default="")
    phone = models.IntegerField(default="")
    dob = models.DateField(default="")
    headline = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    completed = models.BooleanField(default=False)
    info = models.CharField(max_length=25, default="")

    def __init__(self, fname, lname, email, phone, dob, headline, date, completed, info, id):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.dob = dob
        self.headline = headline
        self.date = date
        self.completed = completed
        self.info = info