from django.http import JsonResponse

from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .decode_jwt import decode_jwt
from . import permissions as user_permissions
from .serializers import (
    UserSerializer,
    ChangePasswordSerializer,
    CreateUserSerializer,
)


class RegistrationAPI(generics.GenericAPIView):
    """
    사용자 등록(회원가입)

    ---
    # Parameters
        - username : 사용자ID
        - password : 비밀번호
    """

    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "REGISTRATION_SUCCESE",
                "user_id": user.pk,
                "username": user.username,
            }
        )


class UserList(generics.ListCreateAPIView):
    """
    사용자 조회

    ---
    # Parameters
        - token : 발급받은 토큰

    manager권한만 조회가능
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = decode_jwt(request)
        if type(data) == Response:
            return data
        try:
            user = data

            if user.authority != "manager":
                return Response(
                    {"error_code": "USER_AUTHORITY_IS_NOT_MANAGER"}, status=401
                )
        except User.DoesNotExist:
            return Response({"error_code": "USER_IS_NOT_EXISTS"}, status=400)

        return self.list(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    회원정보 수정/삭제

    ---
    # Parameters
        - token     : 발급받은 토큰
        - username  : 사용자ID
        - authority : 권한

    자기자신 또는 manager권한을 가지고있는 사용자 이용가능
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (user_permissions.IsWriterOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class ChangePasswordView(generics.UpdateAPIView):
    """
    사용자 비밀번호 변경

    ---
    # Parameters
        - token     
        - old_passowrd 
        - new_passowrd  

    자기자신 또는 manager권한을 가지고있는 사용자 이용가능
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = ()
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_object(self, queryset=None):
        data = decode_jwt(self.request)
        if type(data) == Response:
            return data
        return data

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

