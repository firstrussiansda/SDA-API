# -*- coding: utf-8 -*-
"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from configurations import Configuration, values
from django.utils.translation import gettext_lazy as _

from .mixins import (
    DjangoMixin,
    EmailMixin,
    LoggingMixin,
    RichTextMixin,
    SecurityMixin,
)


class Settings(
    LoggingMixin, SecurityMixin, DjangoMixin, EmailMixin, RichTextMixin, Configuration
):
    INSTALLED_APPS_PROJECT = [
        # apps
        "announcements",
        "events",
        "files",
        "media",
        "people",
        "sermons",
        "services",
        "thoughts",
        "redirects",
        "utils",
        # project
        "firstrussian",
    ]
    INSTALLED_APPS_OTHER = [
        # 3rd party apps
        "corsheaders",
        "django_bleach",
        "drf_yasg",
        "modeltranslation",
        "rest_framework",
        "rosetta",
        "tinymce",
    ]

    MIDDLEWARE_RESPONSE_AFTER_MINIFY = [
        "corsheaders.middleware.CorsMiddleware",
        "firstrussian.middleware.locale.LocaleMiddleware",
    ]

    LANGUAGES = (("ru", _("Russian")), ("uk", _("Ukranian")), ("en", _("English")))

    SITE_URL = values.Value(default="/")

    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_METHODS = ["GET", "OPTIONS"]
