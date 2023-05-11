from django.db import models
from django.shortcuts import redirect

# Create your models here.


#user data base to cross reference account information with the cookies
#this is done because it was difficult to access the django account authentication db directly
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

#model to create a data base for all of the flavors any user creates
class Flavor(models.Model):
    def my_view(request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        return redirect(request, "main/base.html",)

    #flavor name
    name = models.CharField(max_length=50, null=True)
    #flavor id
    id = models.IntegerField(primary_key=True)
    #vcpus
    amt_vCPU = models.IntegerField(null=True)
    #mem
    amt_Memory = models.FloatField(null=True)
    #vol
    amt_Volume = models.FloatField(null=True)
    #ephemeral vol
    amt_Ephemeral_Volume = models.FloatField(null=True)
    #acctUsername (this is the only variable saved not by user input, it is automatically saved by reading the user's account name)
    acctUsername = models.CharField(max_length=50, null=True)

    DisplayFields = ['name', 'id', 'amt_vCPU', 'amt_Memory', 'amt_Volume', 'amt_Ephemeral_Volume', 'acctUsername']
    def _str_(self):
        return (self.id + ": " + self.name)

class Predict(models.Model):

    amt_CPU = models.IntegerField(null=True, blank=True)
    amt_vCPU = models.FloatField(null=True, blank=True)
    prcnt_CPU = models.FloatField(null=True, blank=True)

    amt_Memory = models.FloatField(null=True, blank=True)
    prcnt_Memory = models.FloatField(null=True, blank=True)

  

    DisplayFields = ['amt_CPU', 'amt_vCPU', 'prcnt_CPU', 'amt_Memory', 'prcnt_Memory']
    def _str_(self):
        return (self.id + ": " + self.name)
    
    