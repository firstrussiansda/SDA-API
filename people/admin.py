# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Person


@admin.register(Person)
class Person(TranslationAdmin):
    fields = [
        "slug",
        "name",
        "gravatar_email",
        "profile_image",
        "position",
        "about",
    ]
