from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages

from main.forms import FlavorInputForm
from .forms import FlavorInputForm
from .forms import UserInformation
from .models import User
from main.models import Flavor
from .models import Flavor
# Create your views here.

@login_required(login_url='login')
def main(request):
    results = Flavor.objects.all()
    return render(request, "main/home.html", {'acctInfo': results})

def login(request):

    form = UserInformation()

    if request.method == 'POST':
       form = UserInformation(request.POST)

       if form.is_valid():
           form.save()

       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
           auth_login(request, user)
           return redirect('main page')

    context = {'form': form}
    return render(request, "login/login.html")

def create(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login page')

    context = {'form': form}
    return render(request, "create/register.html", context)

@login_required(login_url='login')
def flavor(request):
    form = FlavorInputForm()

    if request.method == 'POST':
        form = FlavorInputForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.acctUsername = request.user
            instance.save()
            return redirect('main page')
            #TODO redirect to flavor display page
    context = {
        'form': form
    }
    return render(request, "flavor/createflavor.html", context)