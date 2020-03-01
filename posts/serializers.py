from rest_framework import serializers
from . import models as post_model


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = post_model.Post
        fields = '__all__'
