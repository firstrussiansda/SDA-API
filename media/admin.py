# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SoundCloudAsset, YouTubeAsset, ZoomAsset


@admin.register(SoundCloudAsset)
class SoundCloudOptions(admin.ModelAdmin):
    list_display = ["title", "html_object_link"]
    fields = [
        "title",
        "object_id",
        "html_object_link",
        "thumbnail_url",
        "thumbnail_override",
        "track_id",
    ]
    readonly_fields = ["title", "html_object_link", "thumbnail_url", "track_id"]


@admin.register(YouTubeAsset)
class YouTubeOptions(admin.ModelAdmin):
    list_display = ["title", "start_at_seconds", "html_object_link"]
    fields = [
        "title",
        "object_id",
        "start_at_seconds",
        "html_object_link",
        "thumbnail_url",
        "thumbnail_override",
    ]
    readonly_fields = ["title", "html_object_link", "thumbnail_url"]


@admin.register(ZoomAsset)
class ZoomAssetOptions(admin.ModelAdmin):
    list_display = ["title", "zoom_link_html"]
    fields = [
        "title",
        "zoom_link",
        "zoom_link_html",
    ]
    readonly_fields = ["zoom_link_html"]
