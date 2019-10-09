from modeltranslation.translator import TranslationOptions, register

from .models import Sermon


@register(Sermon)
class SermonOptions(TranslationOptions):
    fields = ["title", "description"]
