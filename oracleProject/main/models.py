from django.db import models

# Create your models here.
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
    #flavor name
    name = models.CharField(max_length=50)
    #flavor id(?)
    id = models.IntegerField(primary_key=True)
    #vcpus
    amt_vCPU = models.IntegerField()
    #mem
    amt_Memory = models.FloatField()
    #vol
    amt_Volume = models.FloatField()
    #ephemeral vol
    amt_Ephemeral_Volume = models.FloatField()

    def _str_(self):
        return (self.id + ": " + self.name)