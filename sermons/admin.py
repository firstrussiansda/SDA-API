# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Sermon, SermonSeries


class SermonInline(admin.StackedInline):
    model = Sermon
    extra = 1
    filter_horizontal = ["speakers", "soundcloud_assets", "youtube_assets"]


@admin.register(SermonSeries)
class SermonSeriesOptions(TranslationAdmin):
    fields = [
        "title",
        "description",
    ]
    inlines = [SermonInline]


@admin.register(Sermon)
class SermonOptions(TranslationAdmin):
    fields = [
        "date",
        "title",
        "description",
        "series",
        "speakers",
        "soundcloud_assets",
        "youtube_assets",
    ]
    filter_horizontal = ["speakers", "soundcloud_assets", "youtube_assets"]
