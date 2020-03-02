from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsWriterOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


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
        pk = self.request.parser_context['kwargs']["pk"]

        post = Post.objects.get(id=int(pk))
        serializer.save(user=self.request.user, post=post,)
