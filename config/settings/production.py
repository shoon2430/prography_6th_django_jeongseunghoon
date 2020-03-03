from .base import *
import dj_database_url
import django_heroku

WSGI_APPLICATION = "config.wsgi.production.application"

DEBUG = False

ALLOWED_HOSTS = ["*.herokuapp.com"]

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

django_heroku.settings(locals())
