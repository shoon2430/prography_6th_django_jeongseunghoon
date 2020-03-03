from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

# app_name = "users"

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
