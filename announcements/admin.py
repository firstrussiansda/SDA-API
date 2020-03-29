# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Announcement


@admin.register(Announcement)
class ThoughtOptions(TranslationAdmin):
    fields = [
        "slug",
        "title",
        "description",
        "announcement_html",
        "is_featured",
        "alert_level",
        "start_date",
        "end_date",
        "image_url",
        "image_description",
        "attachments",
    ]
    filter_horizontal = [
        "attachments",
    ]
