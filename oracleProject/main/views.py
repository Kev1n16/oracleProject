from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
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

def main(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context = {
            'userID': request.COOKIES['username'],
            'login_status': request.COOKIES.get('login_status'),
            'acctInfo': Flavor.objects.all(),
        }
        return render(request, 'main/base.html', context)
    else:
        return render(request, 'login/login.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        context = {
            'userID': username,
            'login_status': True,
            'acctInfo': Flavor.objects.all(),
        }
        response = render(request, 'main/home.html', context)

        # cookie settings
        response.set_cookie('username', username)
        response.set_cookie('login_status', True)

        return response


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
    form = FlavorInputForm()

    if request.method == 'POST':
        print("hello")
        form = FlavorInputForm(request.POST)
        form.name = request.POST.get('name')
        form.id = request.POST.get('id')
        form.amt_vCPU = request.POST.get('amt_vCPU')
        form.amt_Memory = request.POST.get('amt_Memory')
        form.amt_Volume = request.POST.get('amt_Volume')
        form.amt_Ephemeral_Volume = request.POST.get('amt_Ephemeral_Volume')
        form.acctUsername = request.COOKIES['username']
        username = request.COOKIES['username']

        context = {
            'userID': username,
            'login_status': True,
            'acctInfo': Flavor.objects.all(),
            'name': form.name,
            'id': form.id,
            'amt_vCPU': form.amt_vCPU,
            'amt_Memory': form.amt_Memory,
            'amt_Volume': form.amt_Volume,
            'amt_Ephemeral_Volume': form.amt_Ephemeral_Volume,
            'acctUsername': form.acctUsername,
        }
        response = render(request, 'flavor/createflavor.html', context)
        return response
    print("goodbye")
    return render(request, "main/home.html")


def logout(request):
    response = HttpResponseRedirect(reverse('login page'))

    #deleting cookies
    response.delete_cookie('username')
    response.delete_cookie('login_status')

    return response