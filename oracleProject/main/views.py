from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages
# Create your views here.

def main(request):
    return render(request, "main/home.html",)

def login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)
       if user is not None:
           auth_login(request, user)
           return redirect('main page')

    context = {}
    return render(request, "login/login.html",)

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
    
def flavor(request):
    return render(request, "flavor/createflavor.html",)