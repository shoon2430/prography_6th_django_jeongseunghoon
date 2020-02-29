from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from . import models as post_model


class PostViewSet(viewsets.ModelViewSet):
    queryset = post_model.Post.objects.all()
    serializer_class = PostSerializer
