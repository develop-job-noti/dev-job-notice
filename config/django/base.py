# System
import os
from pathlib import Path
from datetime import timedelta

# Project
from core.constants import SERVICE


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = SERVICE.SECRET_KEY

DEBUG = SERVICE.DEBUG

ALLOWED_HOSTS = SERVICE.ALLOWED_HOSTS

# ==================================================================== #
#                     설치된 앱, 사용하는 앱 config                    #
# ==================================================================== #

LOCAL_APPS = [
    "apis.users",
    "apis.notifications",
    "apis.jobs",
    "apis.filters",
    "core",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_spectacular",
    "django_extensions",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

APPEND_SLASH = False

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # 프로젝트에 전반적으로 사용되는 템플릿이 있다면 여기에서 설정
            # 이렇게 하면은 이제 templates 특정 앱 안에 두게 되는데 특정 앱이 아닌 앱에서 벗어난 경로에 templates 파일은 이렇게 설정해줘야 한다.
            os.path.join(BASE_DIR, "config", "templates"),
        ],
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

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"  # 언어 - 국가 설정

TIME_ZONE = "Asia/Seoul"  # 시간대 설정

USE_I18N = True  # 국제화

# 지역화, 4.0 부터 더 이상 사용되지 않는다. (https://docs.djangoproject.com/en/4.2/ref/settings/#use-l10n)
USE_L10N = True

USE_TZ = False  # 장고 시간대 사용 여부


# ==================================================================== #
#                  file system (static) config                         #
# ==================================================================== #
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# ==================================================================== #
#                       DRF config                                     #
# ==================================================================== #
REST_FRAMEWORK = {
    # 애플리케이션에서 사용할 인증 방법을 정의
    # "DEFAULT_AUTHENTICATION_CLASSES": ("core.authentication.SecureTokenAuthentication",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "EXCEPTION_HANDLER": "core.exception.default_exception_handler",  # 예외 처리기 설정
    # drf의 schema 클래스를 drf-spectacular의 AuthSechema로 교체
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PARSER_CLASSES": [  # 요청 본문을 파싱하는 데  사용할 파서를 지정
        "rest_framework.parsers.JSONParser",  # JSON 파서
    ],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    # "DEFAULT_RENDERER_CLASSES": ("core.renderers.CustomRenderer",),
    "DEFAULT_RESPONSE_CLASS": "core.response.CustomResponse",
    "DEFAULT_PAGINATION_CLASS": "core.pagination.CustomPagination",
}


# ==================================================================== #
#                       Logging config                                 #
# ==================================================================== #
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "django.server": {
            "format": "[%(asctime)s] [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "syslog": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",
            "formatter": "django.server",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "django.server",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "log/django-access.log",
            "formatter": "django.server",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "monitor": {
            "handlers": ["file", "syslog", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "django": {
            "handlers": ["file", "syslog"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
REST_AUTH = {
    "OLD_PASSWORD_FIELD_ENABLED": True,
    "USE_JWT": True,
}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
