"""
Django settings for Trackdéchets assistance project.

"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

INSTALLED_APPS = [
    "grappelli.dashboard",
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.forms",
    "corsheaders",
    "django_hosts",
    "rest_framework",
    "widget_tweaks",
    "adminsortable2",
    "solo",
    "compressor",
    "mptt",
    "martor",
    "template_partials",
    "request",
    "accounts",
    "content",
    "webinars",
    "website",
]

MIDDLEWARE = [
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "config.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "csp.middleware.CSPMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]

ROOT_HOSTCONF = "config.hosts"
DEFAULT_HOST = "website_hosts"
PARENT_HOST = "track.test"

ROOT_URLCONF = "content.assistance_urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

ADMIN_SLUG = env("ADMIN_SLUG")

MARTOR_ENABLE_CONFIGS = {
    "emoji": "true",  # to enable/disable emoji icons.
    "imgur": "false",  # to enable/disable imgur/custom uploader.
    "mention": "false",  # to enable/disable mention
    "jquery": "true",  # to include/revoke jquery (require for admin default django)
    "living": "false",  # to enable/disable live updates in preview
    "spellcheck": "false",  # to enable/disable spellcheck in form textareas
    "hljs": "false",  # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    "bold",
    "italic",
    "horizontal",
    "heading",
    "blockquote",
    "unordered-list",
    "ordered-list",
    "link",
    "emoji",
    "toggle-maximize",
    "help",
]

REQUEST_IGNORE_PATHS = (rf"^{ADMIN_SLUG}/",)

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
}
USE_THOUSAND_SEPARATOR = True
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.trackdechets.beta.gouv.fr$",
]

WEBINARS_DOMAIN = env("WEBINARS_DOMAIN")

GRAPPELLI_ADMIN_TITLE = "Trackdéchets assistance & admin site web"
GRAPPELLI_INDEX_DASHBOARD = "config.dashboard.CustomIndexDashboard"

BREVO_GENERAL_NEWSLETTER_ID = env.int("BREVO_GENERAL_NEWSLETTER_ID")
BREVO_TECH_NEWSLETTER_ID = env.int("BREVO_TECH_NEWSLETTER_ID")
BREVO_API_KEY = env("BREVO_API_KEY")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["http://assistance.track.test"]
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 15768000  # 6 months
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=True)
PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "display-capture": [],
    "document-domain": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "interest-cohort": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

CSP_DEFAULT_SRC = ["'self'", "trackdechets.beta.gouv.fr/", "blob:"]
CSP_SCRIPT_SRC = [
    "'self'",
    "'unsafe-inline'",
    STATIC_URL,
]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    STATIC_URL,
]
CSP_IMG_SRC = [
    "'self'",
    "data:",
    STATIC_URL,
]
CSP_INCLUDE_NONCE_IN = ["script-src", "style-src"]
CSP_FONT_SRC = ("'self'", "data:", STATIC_URL)
CSP_CONNECT_SRC = [
    "'self'",
]
CSP_FRAME_SRC = ("'self'", "https://statistiques.trackdechets.beta.gouv.fr")

BREVO_CATEGORY_FORMULAIRE_SITE_WEB = env("BREVO_CATEGORY_FORMULAIRE_SITE_WEB")
