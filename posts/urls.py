from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

app_name = "posts"

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path("posts/", include(router.urls))
]
