from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _("First Russian Admin")
admin.site.site_title = _("First Russian Admin")
admin.site.site_url = settings.SITE_URL
