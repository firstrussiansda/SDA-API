# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, register

from .models import Thought


@register(Thought)
class ThoughtOptions(TranslationOptions):
    fields = ["title", "description", "thought_html"]
