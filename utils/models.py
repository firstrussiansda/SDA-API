# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django_bleach.models import BleachField


class BleachRichTextField(BleachField, RichTextField):
    """
    Field which both bleaches input and has rich text widget
    """

    def __init__(self, *args, **kwargs) -> None:
        try:
            kwargs.setdefault("verbose_name", args[0])
        except IndexError:  # in migrations
            pass
        super().__init__(*args[1:], **kwargs)
