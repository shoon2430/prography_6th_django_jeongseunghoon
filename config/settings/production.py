from .base import *
import dj_database_url
import django_heroku

WSGI_APPLICATION = "config.wsgi.production.application"

DEBUG = False

ALLOWED_HOSTS = ["*.herokuapp.com"]

DATABASES = {}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

django_heroku.settings(locals())
