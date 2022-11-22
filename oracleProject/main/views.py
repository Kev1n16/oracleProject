from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def main(request):
    return render(request, "main/home.html",)

def login(request):
    return render(request, "login/login.html",)

def create(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "create/register.html", context)
    
def flavor(request):
    return render(request, "flavor/createflavor.html",)