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
    form = UserInformation()

    if request.method == 'GET':
        form = UserInformation(request.POST)
        if form.is_valid():
            form.save()
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
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        print("in")
        context = {
            'userID': request.COOKIES['username'],
            'login_status': request.COOKIES.get('login_status'),
            'acctInfo': Flavor.objects.all(),
        }

        if request.method == 'POST':
            print("inside")
            form = FlavorInputForm(request.POST)
            form = FlavorInputForm(initial={'acctUsername': request.COOKIES['username']})
            form.fields['acctUsername'] = request.COOKIES['username']
            form.fields['name'] = request.POST.get('name')
            form.fields['id'] = request.POST.get('id')
            form.fields['amt_vCPU'] = request.POST.get('amt_vCPU')
            form.fields['amt_Memory'] = request.POST.get('amt_Memory')
            form.fields['amt_Volume'] = request.POST.get('amt_Volume')
            form.fields['amt_Ephemeral_Volume'] = request.POST.get('amt_Ephemeral_Volume')
            print(form.fields['amt_Ephemeral_Volume'])
            print(form.fields['name'])
            print(form.fields['acctUsername'])
            print(form.fields['amt_vCPU'])
            form.save()
            if form.is_valid():
                print("valid")
                instance = form.save(commit=False)
                instance.username = request.user
                form.save()
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