from django.shortcuts import render
from django.contrib.auth import authenticate, login

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from . import models as user_model
import pprint


@api_view(['POST'])
def LoginApiView(request):
    # user = authenticate(username=username, password=password)
    # print(user)
    if request.method == 'POST':
        if request.data:
            try:
                username = request.data['id']
                password = request.data['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    user_info = user_model.User.objects.get(id=user.id)
                    serializer = UserSerializer(user_info)
                    return Response({"message": "login success", "data": serializer.data})

            except Exception:
                return Response({"message": "login fail"})

        return Response({"message": "login fail"})

    return Response({"message": "login fail"})


@api_view(['POST'])
def LogoutApiView(request):
    # user = authenticate(username=username, password=password)
    # print(user)
    if request.method == 'POST':
        if request.data:
            print(request.data)

            return Response({"message": "logout fail"})

        return Response({"message": "logout fail"})

    return Response({"message": "logout fail"})

# {
# "id":"admin",
# "password":"1234"
# }
