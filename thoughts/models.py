# -*- coding: utf-8 -*-
import uuid

from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from files.models import Attachment
from people.models import Person
from utils.url import remove_querystring


class Thought(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    slug = models.SlugField(
        _("Slug"),
        max_length=64,
        blank=True,
        unique=True,
        db_index=True,
        help_text=_(
            "Thought title as it will appear in the URL. "
            "Can only be alphanumeric with hyphens as word delimiter."
        ),
    )

    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True)
    thought_html = RichTextField(_("Thought"))

    date = models.DateField(_("Date"), null=True)

    image_url = models.URLField(
        _("Image URL"),
        max_length=512,
        help_text=_("You can find many free images at unsplash.com"),
    )
    image_description = models.CharField(
        _("Image Description"), max_length=512, blank=True
    )

    authors = models.ManyToManyField(
        Person, related_name="thoughts", verbose_name=_("Authors"), blank=True
    )

    attachments = models.ManyToManyField(
        Attachment,
        related_name="thoughts",
        verbose_name=Attachment._meta.verbose_name_plural,
        blank=True,
    )

    class Meta:
        verbose_name = _("Thought")
        verbose_name_plural = _("Thoughts")

    def clean(self) -> None:
        self.clean_slug()
        self.clean_image_url()
        super().clean()

    def clean_slug(self) -> None:
        if not self.slug:
            if self.title_en:
                self.slug = slugify(self.title_en)
            else:
                raise ValidationError(
                    {"slug": self._meta.get_field("slug").error_messages["blank"]}
                )

    def clean_image_url(self) -> None:
        if self.image_url:
            self.image_url = remove_querystring(self.image_url, hostname="unsplash.com")

    def __str__(self) -> str:
        return f"{self.date} - {self.title}"
