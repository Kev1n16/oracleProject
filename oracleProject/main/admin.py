from django.contrib import admin
from .models import ToDoList, Flavor, User

# Registering models here
admin.site.register(ToDoList)

#setting them to display a certain way within the admin page here
@admin.register(User)
class User(admin.ModelAdmin):
    list_display=User.DisplayFields

@admin.register(Flavor)
class User(admin.ModelAdmin):
    list_display=Flavor.DisplayFields