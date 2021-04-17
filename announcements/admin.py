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
        "attachments",
    ]
    filter_horizontal = [
        "attachments",
    ]
    list_display = [
        "start_date",
        "end_date",
        "is_featured",
        "alert_level",
        "title",
    ]
