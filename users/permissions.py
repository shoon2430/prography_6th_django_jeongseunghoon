from rest_framework import permissions
from rest_framework.response import Response
from .models import User
from .decode_jwt import decode_jwt


class ManagerReadOnly(permissions.BasePermission):
    """
    유저 목록은 Manager권한을 가진 사용자만 조회 가능합니다.
    """

    message = "Adding customersdsds222"

    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return False
        else:
            user = User.objects.get(pk=request.user.pk)
            return user.authority == "manager"


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    유저 정보는 로그인후 자기자신 또는 MANAGER만 조회/수정 가능합니다.
    """

    def has_permission(self, request, view):
        data = decode_jwt(request)
        if type(data) == Response:
            return False
        try:
            jwt_user = data

            if jwt_user.is_anonymous:
                return False

            pk = request.parser_context["kwargs"]["pk"]
            user = User.objects.get(id=pk)
            return jwt_user == user or jwt_user.authority == "manager"

        except User.DoesNotExist:
            return False
