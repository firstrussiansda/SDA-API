# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SoundCloudAsset, YouTubeAsset


@admin.register(SoundCloudAsset)
class SermonOptions(admin.ModelAdmin):
    list_display = ["title", "html_object_link"]
    fields = ["title", "object_id", "html_object_link", "thumbnail_url", "track_id"]
    readonly_fields = ["title", "html_object_link", "thumbnail_url", "track_id"]


@admin.register(YouTubeAsset)
class YouTubeOptions(admin.ModelAdmin):
    list_display = ["title", "html_object_link"]
    fields = ["title", "object_id", "html_object_link", "thumbnail_url"]
    readonly_fields = ["title", "html_object_link", "thumbnail_url"]
