from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

app_name = "users"

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path("users", include(router.urls))
]
