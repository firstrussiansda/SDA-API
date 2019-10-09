"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from configurations import Configuration
from django.utils.translation import gettext_lazy as _

from .mixins import DjangoMixin, LoggingMixin, SecurityMixin


class Settings(LoggingMixin, SecurityMixin, DjangoMixin, Configuration):
    INSTALLED_APPS_PROJECT = [
        # apps
        "events",
        "media",
        "people",
        "sermons",
        # project
        "firstrussian",
    ]
    INSTALLED_APPS_OTHER = [
        # 3rd party apps
        "drf_yasg",
        "modeltranslation",
        "rest_framework",
        "rosetta",
    ]

    MIDDLEWARE_RESPONSE_AFTER_MINIFY = [
        "firstrussian.middleware.locale.LocaleMiddleware"
    ]

    LANGUAGES = (("ru", _("Russian")), ("uk", _("Ukranian")), ("en", _("English")))
