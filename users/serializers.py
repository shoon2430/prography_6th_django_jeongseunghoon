
from rest_framework import serializers
from posts.models import Post
from .models import User


class UserSerializer(serializers.ModelSerializer):

    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all()
    )

    class Meta:
        model = User
        fields = (
            'id',
            "username",
            "authority",
            "posts"
        )
