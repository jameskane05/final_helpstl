from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "helpstl/index.html")

def login(request):
    return render(request, "helpstl/index.html")
    # bullshit value for now