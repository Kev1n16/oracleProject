from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.main, name="main page"),
    path("", views.login, name="login page"),
    path("login/", views.login, name="login page"),
    path("create/", views.create, name="Create account page"),
    path("flavor/", views.flavor, name="flavor"),
    path("logout/", views.logout, name="logout")
]
