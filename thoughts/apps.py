# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ThoughtConfig(AppConfig):
    name = "thoughts"
    verbose_name = _("thoughts")
