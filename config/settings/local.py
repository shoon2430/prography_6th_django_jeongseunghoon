from .base import *
import os
import json

SECRETS = json.load(open(os.path.join(SECRET_DIR, "base.json")))
SECRET_KEY = SECRETS["SECRET_KEY"]

WSGI_APPLICATION = "config.wsgi.local.application"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
