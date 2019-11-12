# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Event


@admin.register(Event)
class EventOptions(TranslationAdmin):
    fields = [
        "date",
        "is_featured",
        "title",
        "description",
        "image_url",
        "image_description",
        "location_name",
        "location_map_name",
        "location_google_maps_link",
    ]
    readonly_fields = ["location_google_maps_link"]
