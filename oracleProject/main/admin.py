from django.contrib import admin
from .models import ToDoList, Flavor, User

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Flavor)
admin.site.register(User)