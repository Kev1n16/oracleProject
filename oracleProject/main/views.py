from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>main page!</h1>")

def login(response):
    return HttpResponse("<h1>Login page!</h1>")

def create(response):
    return HttpResponse("<h1>Create account page!</h1>")