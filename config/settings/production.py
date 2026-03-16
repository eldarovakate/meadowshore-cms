from .base import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    "meadowshore.ru",
    "www.meadowshore.ru",
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://meadowshore.ru",
    "https://www.meadowshore.ru",
    "https://*.onrender.com",
]

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    "default": dj_database_url.config (
        conn_max_age=600,
        ssl_require=True,
    )
}

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedStaticFilesStorage"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

try:
    from .local import *
except ImportError:
    pass