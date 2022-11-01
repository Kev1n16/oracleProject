from django.urls import path

from.import views

urlpatterns = [
path("", views.main, name="main page"),
path("login/", views.login, name="login page"),
path("create/", views.create, name="Create account page"),
]