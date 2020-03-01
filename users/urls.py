from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

app_name = "users"


urlpatterns = [
    path("login/", views.LoginApiView, name="login"),
    path("logout/", views.LogoutApiView, name="logout")
]
