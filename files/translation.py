# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, register

from .models import Attachment


@register(Attachment)
class AttachmentOptions(TranslationOptions):
    fields = ["name"]
