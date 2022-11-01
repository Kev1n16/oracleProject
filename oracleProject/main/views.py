from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(response):
    return HttpResponse("<h1>Main page!</h1>")

def login(response):
    return HttpResponse("<h1>Login page!</h1>")

def create(response):
    return render(response, "templates/main/base.html", {})

"""Still trying to link this to an actual html file
def create(response):
    return render(response, "templates/main/base.html", {})
    ...doesnt work"""