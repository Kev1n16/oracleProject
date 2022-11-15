from django.shortcuts import render

# Create your views here.
def register(response):
    form = UserCreationFrom()
    return render(response, "register/register.html", {"form":form})