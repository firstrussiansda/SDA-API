# -*- coding: utf-8 -*-
import typing
import uuid

from django.db import models
from django.utils.http import urlquote
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from files.models import Attachment
from utils.url import remove_querystring


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
    location_map_name = models.CharField(
        _("Location Map Name"),
        max_length=255,
        blank=True,
        help_text=_(
            "Location name to search in Google Maps. "
            "Should be unique to result in single search result."
        ),
    )

    attachments = models.ManyToManyField(
        Attachment,
        related_name="events",
        verbose_name=Attachment._meta.verbose_name_plural,
        blank=True,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def clean(self) -> None:
        self.clean_image_url()
        super().clean()

    def clean_image_url(self) -> None:
        if self.image_url:
            self.image_url = remove_querystring(self.image_url, hostname="unsplash.com")

    def __str__(self) -> str:
        return f"{self.date} - {self.title}"

    @property
    def location_google_maps_url(self) -> typing.Optional[str]:
        return (
            f"https://google.com/maps/place/{urlquote(self.location_map_name)}"
            if self.location_map_name
            else None
        )

    @property
    def location_google_maps_link(self) -> str:
        return (
            typing.cast(
                str,
                mark_safe(
                    f'<a target="blank" href={self.location_google_maps_url}>{self.location_google_maps_url}</a>'
                ),
            )
            if self.location_google_maps_url
            else ""
        )
