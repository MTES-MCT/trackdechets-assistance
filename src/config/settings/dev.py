from .base import *  # noqa

DEBUG = True

SECRET_KEY = "xyzabcdefghu"

INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp-providenzpro.alwaysdata.net"
EMAIL_HOST_PASSWORD = "supermailer"
EMAIL_HOST_USER = "mailer@providenz.fr"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
MESSAGE_RECIPIENT = "lp@providenz.fr"
