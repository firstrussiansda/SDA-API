from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SermonsConfig(AppConfig):
    name = "sermons"
    verbose_name = _("sermons")
