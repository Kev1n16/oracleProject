from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
define register(response):
    form = userCreationForm()
    return render(response, "register/register.html", {"form": form})