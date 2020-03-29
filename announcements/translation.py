# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, register

from .models import Announcement


@register(Announcement)
class AnnouncementOptions(TranslationOptions):
    fields = ["title", "description", "announcement_html"]
