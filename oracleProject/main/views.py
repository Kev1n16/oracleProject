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


@login_required(login_url='login')
def flavor(request):
    form = FlavorInputForm()

    if request.method == 'POST':
        form = FlavorInputForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect('main page')
            # TODO redirect to flavor display page
    context = {
        'form': form
    }
    return render(request, "flavor/createflavor.html", context)


def logout(request):
    response = HttpResponseRedirect(reverse('login page'))

    #deleting cookies
    response.delete_cookie('username')
    response.delete_cookie('login_status')

    return response