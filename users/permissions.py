from rest_framework import permissions
from .models import User


class ManagerReadOnly(permissions.BasePermission):
    """
    유저 목록은 Manager권한을 가진 사용자만 조회 가능합니다.
    """

    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return False
        else:
            user = User.objects.get(pk=request.user.pk)
            return user.authority == "manager"


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    유저 정보는 로그인후 자기자신만 수정가능합니다.
    """

    def has_permission(self, request, view):
        try:
            if request.user.is_anonymous:
                return False

            pk = request.parser_context['kwargs']["pk"]
            user = User.objects.get(id=pk)
            return request.user == user or request.user.authority == "manager"

        except User.DoesNotExist:
            return False
