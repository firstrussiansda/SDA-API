# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Attachment


@admin.register(Attachment)
class AttachmentOptions(TranslationAdmin):
    fields = ["name", "file", "checksum"]
    readonly_fields = ["checksum"]
