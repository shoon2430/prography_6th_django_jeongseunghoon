import jwt
import json
from django.http import JsonResponse
from rest_framework.response import Response
from config.settings.base import SECRET_KEY

from .models import User


def decode_jwt(request):
    if "Authorization" not in request.headers:
        return Response({"error_code": "AUTHORIZATION_NOT_FIND"}, status=401)

    encode_token = request.headers["Authorization"]
    try:
        data = jwt.decode(encode_token, SECRET_KEY, algorithm="HS256")
        user = User.objects.get(id=data["user_id"])
        return user

    except jwt.DecodeError:
        return Response({"error_code": "INVALID_TOKEN"}, status=401)
    except User.DoesNotExist:
        return Response({"error_code": "UNKNOWN_USER"}, status=401)
