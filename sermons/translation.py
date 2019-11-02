# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, register

from .models import Sermon, SermonSeries


@register(SermonSeries)
class SermonSeriesOptions(TranslationOptions):
    fields = ["title", "description"]


@register(Sermon)
class SermonOptions(TranslationOptions):
    fields = ["title", "description"]
