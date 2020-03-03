from django.urls import path
from . import views

# app_name = "posts"

urlpatterns = [
    path("/posts", views.PostList.as_view()),
    path("/posts/<int:pk>", views.PostDetail.as_view()),
    path("/posts/<int:pk>/comments", views.CommentList.as_view()),
]
