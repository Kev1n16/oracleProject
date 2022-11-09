from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, "main/home.html",)

def login(request):
    return render(request, "login/login.html",)

def create(request):
    return render(request, "create/createaccount.html",)

"""Still trying to link this to an actual html file
def create(response):
    return render(response, "templates/main/base.html", {})
    ...doesnt work"""