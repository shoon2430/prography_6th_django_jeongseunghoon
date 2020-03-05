from rest_framework import serializers
from posts.models import Post
from .models import User
from django.contrib import auth


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    """
       Serializer for password change endpoint.
       """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):

    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "authority", "posts")

