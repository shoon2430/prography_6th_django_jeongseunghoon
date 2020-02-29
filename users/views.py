from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from . import models as user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_model.User.objects.all()
    serializer_class = UserSerializer
