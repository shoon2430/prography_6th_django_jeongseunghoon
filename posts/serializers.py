from rest_framework import serializers
from .models import Post, Comment
from users import serializers as user_serializers


class PostSerializer(serializers.ModelSerializer):

    writer = serializers.ReadOnlyField(source="writer.username")
    # comments = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Comment.objects.all()
    # )

    class Meta:
        model = Post
        fields = (
            'id',
            'writer',
            'title',
            'description',
            # 'comments',
            'created',
            'updated',
        )


class CommentSerializer(serializers.ModelSerializer):

    post = serializers.ReadOnlyField(source="post.title")
    post_id = serializers.ReadOnlyField(source="post.pk")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "post_id",
            "user",
            "contents",
            "visibility",
            'created',
            'updated',
        )
