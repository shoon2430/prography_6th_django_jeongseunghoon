from rest_framework import generics, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsWriterOrReadOnly


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        name = self.request.query_params.get("name", None)

        if name:
            queryset = queryset.filter(writer__username=name)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        GET 게시물을 데이터 불러오기
        ---
        # filter
            name : 사용자ID

        # QUERY PARAMETERS 가 없을 경우 전체 데이터 호출
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        POST 게시물을 생성
        ---
        # 내용
            로그인시 생성가능

            - title : 제목
            - description : 내용
        """
        return self.create(request, *args, **kwargs)


class PostCategoryList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsWriterOrReadOnly,
    )


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        pk = self.request.parser_context["kwargs"]["pk"]

        post = Post.objects.get(id=int(pk))
        serializer.save(
            user=self.request.user, post=post,
        )
