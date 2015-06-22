from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.helpstl, name="helpstl"),
    url(r'^request.html$', views.request, name="request")
]