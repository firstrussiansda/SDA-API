# -*- coding: utf-8 -*-
import hashlib
import pathlib
import socket
import typing

from configurations import values


class DjangoMixin:
    DEVELOPMENT = values.BooleanValue(default=False)

    @property
    def DEBUG(self) -> bool:
        return typing.cast(
            bool, values.BooleanValue(default=self.DEVELOPMENT, environ_name="DEBUG")
        )

    # where manage.py is located
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent.parent.parent
    # project name - name of PROJECT_PATH inside project root
    PROJECT_NAME = pathlib.Path(__file__).resolve().parent.parent.parent.name

    @property
    def ROOT_URLCONF(self) -> str:
        return f"{self.PROJECT_NAME}.urls"

    STATIC_URL = "/static/"

    @property
    def MEDIA_URL(self) -> str:
        if self.DEVELOPMENT:
            return "/media/"
        else:
            return f"https://s3.amazonaws.com/{self.AWS_STORAGE_BUCKET_NAME}/"

    STATIC_ROOT = values.PathValue(
        default=str(pathlib.Path(PROJECT_PATH) / PROJECT_NAME / "static")
    )
    MEDIA_ROOT = values.PathValue(
        default=str(pathlib.Path(PROJECT_PATH) / PROJECT_NAME / "media")
    )

    @property
    def STATICFILES_STORAGE(self) -> str:
        if self.DEVELOPMENT:
            return "django.contrib.staticfiles.storage.StaticFilesStorage"
        else:
            return "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

    @property
    def DEFAULT_FILE_STORAGE(self) -> str:
        if self.DEVELOPMENT:
            return "django.core.files.storage.FileSystemStorage"
        else:
            return "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = values.Value()
    AWS_S3_REGION_NAME = values.Value()
    AWS_DEFAULT_ACL = None

    @property
    def WSGI_APPLICATION(self) -> str:
        return f"{self.PROJECT_NAME}.wsgi.application"

    DATABASES = values.DatabaseURLValue(
        default="sqlite:///db.sqlite3", conn_max_age=None, environ_prefix="DJANGO"
    )

    INSTALLED_APPS_PROJECT: typing.List[str] = []
    INSTALLED_APPS_OTHER: typing.List[str] = []
    INSTALLED_APPS_CONTRIB = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
    ]
    INSTALLED_APPS_DEV = [
        # conditially added when DEVELOPMENT=True
        "debug_toolbar",
        "django_extensions",
    ]

    @property
    def INSTALLED_APPS(self) -> typing.List[str]:
        additional = self.INSTALLED_APPS_DEV if self.DEVELOPMENT else []
        return (
            self.INSTALLED_APPS_PROJECT
            + additional
            + self.INSTALLED_APPS_OTHER
            + self.INSTALLED_APPS_CONTRIB
        )

    MIDDLEWARE_RESPONSE_BEFORE_COMPRESSION: typing.List[str] = []
    MIDDLEWARE_RESPONSE_AFTER_COMPRESSION: typing.List[str] = []
    MIDDLEWARE_RESPONSE_BEFORE_MINIFY: typing.List[str] = []
    MIDDLEWARE_RESPONSE_AFTER_MINIFY: typing.List[str] = []

    @property
    def MIDDLEWARE(self) -> typing.List[str]:
        return [
            i
            for i in (
                ["firstrussian.middleware.structlog.StructLogMiddleware"]
                + self.MIDDLEWARE_RESPONSE_AFTER_COMPRESSION
                + [
                    (
                        "django.middleware.gzip.GZipMiddleware"
                        if not self.DEVELOPMENT
                        else None
                    )
                ]
                + self.MIDDLEWARE_RESPONSE_BEFORE_COMPRESSION
                + [
                    (
                        "django.middleware.security.SecurityMiddleware"
                        if not self.DEVELOPMENT
                        else None
                    ),
                    (
                        "firstrussian.middleware.whitenoise.StaticAndMediaMiddleware"
                        if not self.DEVELOPMENT
                        else None
                    ),
                    (
                        "debug_toolbar.middleware.DebugToolbarMiddleware"
                        if "debug_toolbar" in self.INSTALLED_APPS
                        else None
                    ),
                    (
                        "django.contrib.sessions.middleware.SessionMiddleware"
                        if "django.contrib.sessions" in self.INSTALLED_APPS
                        else None
                    ),
                    "django.middleware.common.CommonMiddleware",
                    "django.middleware.csrf.CsrfViewMiddleware",
                    (
                        "django.contrib.auth.middleware.AuthenticationMiddleware"
                        if "django.contrib.auth" in self.INSTALLED_APPS
                        else None
                    ),
                    (
                        "django.contrib.messages.middleware.MessageMiddleware"
                        if "django.contrib.messages" in self.INSTALLED_APPS
                        else None
                    ),
                    "django.middleware.clickjacking.XFrameOptionsMiddleware",
                    (
                        "django.middleware.locale.LocaleMiddleware"
                        if self.USE_I18N
                        else None
                    ),
                ]
                + self.MIDDLEWARE_RESPONSE_AFTER_MINIFY
                + ["django_auxilium.middleware.html.MinifyHTMLMiddleware"]
                + self.MIDDLEWARE_RESPONSE_BEFORE_MINIFY
            )
            if i is not None
        ]

    ALLOWED_HOSTS = values.ListValue(default=["*"])

    @property
    def SECRET_KEY(self) -> str:
        kwargs = {}
        cls = values.SecretValue

        if self.DEVELOPMENT:
            cls = values.Value
            kwargs["default"] = hashlib.sha256(
                f"{self.PROJECT_NAME}{socket.gethostname()}".encode("utf-8")
            ).hexdigest()

        return typing.cast(str, cls(environ_name="SECRET_KEY", **kwargs))

    @property
    def TEMPLATES(self):
        return [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        i
                        for i in [
                            "django.template.context_processors.debug",
                            "django.template.context_processors.request",
                            "django.template.context_processors.media",
                            "django.template.context_processors.static",
                            (
                                "django.template.context_processors.i18n"
                                if self.USE_I18N
                                else None
                            ),
                            (
                                "django.template.context_processors.tz"
                                if self.USE_TZ
                                else None
                            ),
                            (
                                "django.contrib.auth.context_processors.auth"
                                if "django.contrib.auth" in self.INSTALLED_APPS
                                else None
                            ),
                            (
                                "django.contrib.messages.context_processors.messages"
                                if "django.contrib.messages" in self.INSTALLED_APPS
                                else None
                            ),
                        ]
                        if i
                    ]
                },
            }
        ]

    LANGUAGE_CODE = values.Value(default="en")
    TIME_ZONE = "America/New_York"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]

    @property
    def DEBUG_TOOLBAR_CONFIG(self):
        return {"SHOW_TOOLBAR_CALLBACK": lambda r: self.DEVELOPMENT}

    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "firstrussian.pagination.PageNumberPagination",
        "PAGE_SIZE": 100,
    }
