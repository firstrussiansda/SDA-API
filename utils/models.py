# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django_bleach.models import BleachField


class BleachRichTextField(BleachField, RichTextField):
    """
    Field which both bleaches input and has rich text widget
    """
