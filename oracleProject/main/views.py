from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from .models import Flavor
from main.machinelearning import machineLearning

# Create your views here.
def main(request):
    # ensure the username saved from the cookies matches the logged in user's account name
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context = {  # context must be consistent with all views except create
            'userID': request.COOKIES['username'],
            'login_status': request.COOKIES.get('login_status'),
            'acctInfo': Flavor.objects.all(),
        }
        # since its successful return with context
        return render(request, 'main/base.html', context)
    else:
        # else bring user back to login page
        return render(request, 'login/login.html')


def login(request):
    form = UserInformation()

    if request.method == 'GET':  # obtain information from user input
        form = UserInformation(request.POST)
        if form.is_valid():  # check if the information fits the form
            form.save()  # if so save it
        return render(request, 'login/login.html')

    if request.method == 'POST':
        # save the user's inputted username
        username = request.POST.get('username')
        context = {
            'userID': username,
            'login_status': True,
            'acctInfo': Flavor.objects.all(),
        }
        response = render(request, 'main/base.html', context)

        # cookie settings
        # save the username in cookies
        response.set_cookie('username', username)
        # set boolean login_status to true
        response.set_cookie('login_status', True)

        return response


def create(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # save information
        if form.is_valid():  # as long as it is valid it will be saved
            form.save()
            # ensure it is a unique username
            user = form.cleaned_data.get('username')
            # prompt the user that the account was created
            messages.success(request, 'Account was created for ' + user)

            # user will see the success that it was created at the login page
            return redirect('login page')

    context = {'form': form}
    return render(request, "create/register.html", context)


def flavor(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:  # make sure the user is logged in
        context = {
            'userID': request.COOKIES['username'],
            'login_status': request.COOKIES.get('login_status'),
            'acctInfo': Flavor.objects.all(),
        }

        if request.method == 'POST':  # save all of the user's inputs, these will be the same as the attributes in the flavor form
            acctUsername = request.COOKIES['username']
            name = request.POST.get("name")
            id = request.POST.get("id")
            amt_vCPU = request.POST.get("amt_vCPU")
            amt_Memory = request.POST.get("amt_Memory")
            amt_Volume = request.POST.get("amt_Volume")
            amt_Ephemeral_Volume = request.POST.get("amt_Ephemeral_Volume")
            data = Flavor(name=name, id=id, amt_vCPU=amt_vCPU,  # now we save the values into the flavor to store it in the data base
                          amt_Memory=amt_Memory, amt_Volume=amt_Volume, amt_Ephemeral_Volume=amt_Ephemeral_Volume,
                          acctUsername=acctUsername)
            data.save()  # save it here
            return render(request, 'main/base.html', context)

    context = {
        'userID': request.COOKIES['username'],
        'login_status': request.COOKIES.get('login_status'),
        'acctInfo': Flavor.objects.all(),
    }
    return render(request, "flavor/createflavor.html", context)


def logout(request):
    response = HttpResponseRedirect(reverse('login page'))

    # deleting cookies when we log out
    response.delete_cookie('username')
    response.delete_cookie('login_status')

    return response


def predict(request):
    form = PredictInputForm()

    if request.method == 'POST':
        form = PredictInputForm(request.POST)
        data = request.POST
        data = {key: data[key] for key in [
            'amt_CPU', 'amt_vCPU', 'prcnt_CPU', 'amt_Memory', 'used_Memory']}
        # print(data)
        
        if form.is_valid():
            print('Form submitted')
            context = machineLearning(data)
            # print(dictTest)
            return render(request, "predict/predictResults.html", context)
    context = {
        'form': form
    }
    return render(request, "predict/predictflavor.html", context)
