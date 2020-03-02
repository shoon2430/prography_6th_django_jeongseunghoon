from rest_framework import permissions


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    자신이 작성한 글만 수정/삭제 가능
    """

    def has_object_permission(self, request, view, obj):

        # print(request.method)
        # print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.writer == request.user
