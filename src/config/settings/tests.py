from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "td_website_test",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # faster hashes

SECRET_KEY = "xyz12345"

MESSAGE_RECIPIENTS = ["lorem@ipsum.lol"]
ALLOWED_HOSTS = ["*"]  # for host based testing
