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
    ]
