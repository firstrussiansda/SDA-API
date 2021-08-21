# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceOptions(admin.ModelAdmin):
    fields = [
        "datetime",
        "program_html",
        "subscribers",
        "youtube_stream",
        "html_youtube_link",
        "zoom_meeting",
        "html_zoom_link",
        "sermons",
    ]
    readonly_fields = [
        "html_youtube_link",
        "html_zoom_link",
    ]
    filter_horizontal = ["sermons", "subscribers"]
    list_display = [
        "datetime",
        "html_youtube_link",
    ]

    def get_queryset(self, request):
        return Service.objects.select_related("youtube_stream").all()
