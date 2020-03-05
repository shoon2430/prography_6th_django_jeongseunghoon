from rest_framework import serializers
from .models import Post, Comment
from users import serializers as user_serializers


class PostSerializer(serializers.ModelSerializer):

    writer = serializers.ReadOnlyField(source="writer.username")

    class Meta:
        model = Post
        fields = (
            "id",
            "writer",
            "category",
            "title",
            "description",
            "created",
            "updated",
        )


class CommentSerializer(serializers.ModelSerializer):

    post = serializers.ReadOnlyField(source="post.title")
    post_id = serializers.ReadOnlyField(source="post.pk")
    post_category = serializers.ReadOnlyField(source="post.category")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "post_id",
            "post_category",
            "user",
            "contents",
            "visibility",
            "created",
            "updated",
        )
