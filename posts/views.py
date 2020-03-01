from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes

from rest_framework.decorators import action
from rest_framework import viewsets

from . import paginations
from . import models as post_model
from .serializers import PostSerializer


class APIRootView(APIView):
    def get(self, request):
        data = {
            'year-summary-url': reverse('posts-list', request=request)
        }
        return Response(data)


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = post_model.Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    pagination_class = paginations.PostsPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        id = self.request.query_params.get("id", '')
        if id:
            queryset = queryset.get(id=id)

        return queryset

    @action(detail=False)
    def get_post(self, request):
        print(vars(request))
        qs = self.queryset.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def public_list(self, request):
        qs = self.queryset.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
