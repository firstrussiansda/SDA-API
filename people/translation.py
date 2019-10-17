from modeltranslation.translator import TranslationOptions, register

from .models import Person


@register(Person)
class PersonOptions(TranslationOptions):
    fields = ["name", "position", "about"]
