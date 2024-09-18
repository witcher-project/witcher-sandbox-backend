import os
from pathlib import Path

import environ

env = environ.Env()

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

env_path = BASE_DIR / ".env"
if env_path.is_file():
    environ.Env.read_env(env_file=str(env_path))

SECRET_KEY = env("SECRET_KEY", cast=str, default="xJr6pbf@CI8tWszMep3SytO*wdV82J89")
DEBUG = env("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=list, default=["*"])


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_filters",
    "rest_framework",
    "rest_framework_api_key",
    "drf_spectacular",
    "polymorphic",
]

LOCAL_APPS = [
    "witcher_sandbox.core",
    "witcher_sandbox.apps.user",
    "witcher_sandbox.apps.item",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "witcher_sandbox.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "witcher_sandbox.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    }
}


# Password validation

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"

MEDIA_ROOT = "/vol/web/media/"
STATIC_ROOT = "/vol/web/static/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

API_KEY_CUSTOM_HEADER = "HTTP_API_KEY"

SPECTACULAR_SETTINGS = {
    "COMPONENT_SPLIT_REQUEST": True,
}
