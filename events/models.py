# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel


class Event(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True)

    date = models.DateField(_("Date"), null=True)
    is_featured = models.BooleanField(_("Is Featured"), default=False)

    image_url = models.URLField(
        _("Image URL"),
        max_length=512,
        help_text=_("You can find many free images at unsplash.com"),
    )
    image_description = models.CharField(
        _("Image Description"), max_length=512, blank=True
    )

    location_name = models.CharField(_("Location Name"), max_length=256, blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return f"{self.date} - {self.title}"
