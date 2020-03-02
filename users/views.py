from rest_framework import generics, permissions

from .models import User

from . import permissions as user_permissions
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        user_permissions.ManagerReadOnly
    )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        user_permissions.IsWriterOrReadOnly
    )
