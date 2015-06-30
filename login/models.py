from django.db import models
from django.contrib.auth.models import User
from helpstl.models import HelpRequest

class HelpUser():
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=15)
    zip = models.CharField(max_length=6)
