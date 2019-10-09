from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Sermon


@admin.register(Sermon)
class SermonOptions(TranslationAdmin):
    fields = [
        "date",
        "title",
        "description",
        "speakers",
        "soundcloud_assets",
        "youtube_assets",
    ]
    filter_horizontal = ["speakers", "soundcloud_assets", "youtube_assets"]
