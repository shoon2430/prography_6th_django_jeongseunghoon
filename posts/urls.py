from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

app_name = "posts"


post_list = views.PostViewSet.as_view({
    'get': 'list',
})

post_info = views.PostViewSet.as_view({
    'get': 'retrieve',
})


post_create = views.PostViewSet.as_view({
    'post': 'create',
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create),
    path("<int:pk>/", post_info),
    path("<int:pk>/detail/", post_detail),
]
