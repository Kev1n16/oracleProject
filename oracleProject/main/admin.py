from django.contrib import admin
from .models import ToDoList, Flavor, User

# Register your models here.
admin.site.register(ToDoList)

@admin.register(User)
class User(admin.ModelAdmin):
    list_display=User.DisplayFields

@admin.register(Flavor)
class User(admin.ModelAdmin):
    list_display=Flavor.DisplayFields