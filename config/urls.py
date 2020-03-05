"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)

from users import views as user_views

schema_url_v1_patterns = [
    path("token/", obtain_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path("registration/", user_views.RegistrationAPI.as_view()),
    path("api/v1/", include("users.urls")),
    path("api/v1/", include("posts.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="프로그라피 사전과제 Django REST API",
        default_version="v1",
        description="프로그라피 사전과제",
        contact=openapi.Contact(email="shoon2430@gmail.com"),
    ),
    validators=["flex"],  # , "ssv"],
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        "swagger/v1",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("core.urls")),
    url("doc/v1", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("registration/", user_views.RegistrationAPI.as_view()),
    path("token/", obtain_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path("admin/", admin.site.urls),
    path("api/v1/", include("users.urls")),
    path("api/v1/", include("posts.urls")),
]
