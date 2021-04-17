# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Sermon, SermonSeries


class SermonInline(admin.StackedInline):
    model = Sermon
    extra = 1
    filter_horizontal = [
        "speakers",
        "soundcloud_assets",
        "youtube_assets",
        "attachments",
    ]


@admin.register(SermonSeries)
class SermonSeriesOptions(TranslationAdmin):
    fields = [
        "slug",
        "title",
        "description",
    ]
    inlines = [SermonInline]


@admin.register(Sermon)
class SermonOptions(TranslationAdmin):
    fields = [
        "date",
        "is_published",
        "slug",
        "title",
        "description",
        "series",
        "speakers",
        "soundcloud_assets",
        "youtube_assets",
        "attachments",
    ]
    filter_horizontal = [
        "speakers",
        "soundcloud_assets",
        "youtube_assets",
        "attachments",
    ]
    list_filter = [
        "series",
        "speakers",
        "date",
    ]
    list_display = [
        "date",
        "is_published",
        "title",
        "series",
    ]

    def get_queryset(self, request):
        return Sermon.all_sermons.all()
