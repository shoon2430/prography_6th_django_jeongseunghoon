from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# app_name = "posts"

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("<int:pk>/comments", views.CommentList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
