from rest_framework import serializers
from . import models as user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model.User
        fields = (
            'id',
            "username",
            "authority",
        )
