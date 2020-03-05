from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from . import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.decode_jwt import decode_jwt


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        name = self.request.query_params.get("name", None)
        category = self.request.query_params.get("category", None)

        if category:
            queryset = queryset.filter(category=category)
        if name:
            queryset = queryset.filter(writer__username=name)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        게시물을 데이터 불러오기

        ---
        # Filter
            name     : 사용자ID
            category : 카테고리

        QUERY PARAMETERS 가 없을 경우 전체 데이터 호출
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        게시물을 생성

        ---
        # Parameters
            - token       : 발급받은 토큰
            - title       : 제목
            - description : 내용
        """
        data = decode_jwt(request)
        if type(data) == Response:
            return data
        request.user = data
        return self.create(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        게시물 수정/삭제

        ---
        # Parameters
            - token       : 발급받은 토큰
            - category    : 카테고리
            - title       : 제목
            - description : 내용
        """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsWriterOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)


class Comments(generics.ListAPIView):
    """
        전체 댓글 조회

        ---
        # Filter
            name     : 사용자ID
            category : 카테고리

    """

    queryset = Comment.objects.all().order_by("post", "created")
    serializer_class = CommentSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = Comment.objects.all()
        name = self.request.query_params.get("name", None)
        category = self.request.query_params.get("category", None)
        if category:
            queryset = queryset.filter(post__category=category)
        if name:
            queryset = queryset.filter(user__username=name)
        return queryset


class PostsComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = ()
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        pk = self.request.parser_context["kwargs"]["pk"]
        post = Post.objects.get(pk=pk)

        queryset = Comment.objects.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        pk = self.request.parser_context["kwargs"]["pk"]

        post = Post.objects.get(id=int(pk))
        serializer.save(
            user=self.request.user, post=post,
        )

    def get(self, request, *args, **kwargs):
        """
        GET 게시물을 댓글 데이터 불러오기

        ---
        # Filter
            name : 사용자ID

        QUERY PARAMETERS 가 없을 경우 전체 데이터 호출
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        POST 게시물 댓글 생성

        ---
        # Parameters
            - token       : 발급받은 토큰
            - title       : 제목
            - description : 내용
        """
        data = decode_jwt(request)
        if type(data) == Response:
            return data
        request.user = data
        return self.create(request, *args, **kwargs)


class PostCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        댓글 수정/삭제

        ---
        # Parameters
            - token       : 발급받은 토큰
            - contents    : 내용
            - visibility  : 공개여부
        """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = ()
    permission_classes = (permissions.IsWriterOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
