# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField
from modeltranslation.manager import MultilingualManager
from tinymce import HTMLField

from .translation import MultilingualFilterQuerySet


class BleachRichTextField(BleachField, HTMLField):  # RichTextField):
    """
    Field which both bleaches input and has rich text widget
    """

    def __init__(self, *args, **kwargs) -> None:
        try:
            kwargs.setdefault("verbose_name", args[0])
        except IndexError:  # in migrations
            pass
        super().__init__(*args[1:], **kwargs)

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        # temporary fix until https://github.com/marksweb/django-bleach/issues/21 is resolved
        field.required = not self.blank
        field.widget = HTMLField.formfield(self, **kwargs).widget
        return field


class SlugFromNameMixin(models.Model):
    """
    Automatically generate slug if not provided
    """

    slug = models.SlugField(
        _("Slug"),
        max_length=128,
        blank=True,
        unique=True,
        db_index=True,
        help_text=_(
            "URL-friendly name. "
            "Can only be alphanumeric with hyphens as word delimiter."
        ),
    )

    class Meta:
        abstract = True

    def clean(self) -> None:
        self.clean_slug()
        super().clean()

    def clean_slug(self) -> None:
        if not self.slug:
            slug_attrs = [getattr(self, i, None) for i in ["name_en", "title_en"]]
            slug_attr = next(filter(None, slug_attrs), None)

            if slug_attr:
                self.slug = slugify(slug_attr)
            else:
                raise ValidationError(
                    {"slug": self._meta.get_field("slug").error_messages["blank"]}
                )


class FilteredTranslatableMixin(models.Model):
    objects = MultilingualManager.from_queryset(MultilingualFilterQuerySet)()
    filterable = MultilingualManager.from_queryset(MultilingualFilterQuerySet)()

    class Meta:
        abstract = True
