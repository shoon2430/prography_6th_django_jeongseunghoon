from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

app_name = "users"
urlpatterns = [
    path("", views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
