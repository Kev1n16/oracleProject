from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    remember = models.CharField(max_length=3)
    DisplayFields = ['username', 'password', 'remember']
    def _str_(self):
        return (self.name)


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def _str_(self):
        return self.text


class Flavor(models.Model):
    def my_view(request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        return redirect(request, "main/home.html",)

    #flavor name
    name = models.CharField(max_length=50, null=True)
    #flavor id(?)
    id = models.IntegerField(primary_key=True)
    #vcpus
    amt_vCPU = models.IntegerField(null=True)
    #mem
    amt_Memory = models.FloatField(null=True)
    #vol
    amt_Volume = models.FloatField(null=True)
    #ephemeral vol
    amt_Ephemeral_Volume = models.FloatField(null=True)
    #acctUsername
    acctUsername = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

    DisplayFields = ['name', 'id', 'amt_vCPU', 'amt_Memory', 'amt_Volume', 'amt_Ephemeral_Volume', 'acctUsername']
    def _str_(self):
        return (self.id + ": " + self.name)