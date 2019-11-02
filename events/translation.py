# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, register

from .models import Event


@register(Event)
class EventOptions(TranslationOptions):
    fields = ["title", "description"]
