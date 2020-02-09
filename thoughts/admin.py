# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Thought


@admin.register(Thought)
class ThoughtOptions(TranslationAdmin):
    fields = [
        "date",
        "title",
        "description",
        "image_url",
        "image_description",
        "thought_html",
        "authors",
        "attachments",
    ]
    filter_horizontal = [
        "authors",
        "attachments",
    ]
