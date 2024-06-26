import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa
from .base import env

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOST")

ADMINS = [el.split(":") for el in env.list("DJANGO_ADMINS", default=[])]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
MESSAGE_RECIPIENT = env("MESSAGE_RECIPIENT")
PARENT_HOST = env("PARENT_HOST")

SECURE_SSL_REDIRECT = True

# django-compressor
# https://django-compressor.readthedocs.io/en/stable/settings.html#django.conf.settings.COMPRESS_ENABLED
COMPRESS_ENABLED = env.bool("COMPRESS_ENABLED", default=True)
# https://django-compressor.readthedocs.io/en/stable/settings.html#django.conf.settings.COMPRESS_URL
COMPRESS_URL = STATIC_URL  # noqa F405
# https://django-compressor.readthedocs.io/en/stable/settings.html#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True  # Offline compression is required when using Whitenoise

SENTRY_URL = env("SENTRY_URL")


def traces_sampler(ctx):
    """Exclude statics from traces."""
    if "wsgi_environ" in ctx:
        url = ctx["wsgi_environ"].get("PATH_INFO", "")
        if url.startswith("/static/"):
            return 0
    return 0.1


sentry_sdk.init(
    dsn=SENTRY_URL,
    integrations=[
        DjangoIntegration(),
    ],
    traces_sampler=traces_sampler,
)
