from rest_framework import permissions
from users.decode_jwt import decode_jwt
from rest_framework.response import Response
from .models import Post


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    자신이 작성한 글만 수정/삭제 가능
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
            post = Post.objects.get(id=pk)

            return post.writer == jwt_user or jwt_user.authority == "manager"

        except Post.DoesNotExist:
            return False
