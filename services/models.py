# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from media.models import YouTubeAsset
from people.models import Person
from sermons.models import Sermon
from utils.models import BleachRichTextField


class Service(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    datetime = models.DateTimeField(_("Time"), null=False)

    program_html = BleachRichTextField(_("Program"), blank=True)

    subscribers = models.ManyToManyField(
        Person, related_name="services", verbose_name=_("Subscribers"), blank=True
    )

    youtube_stream = models.ForeignKey(
        YouTubeAsset,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="services",
        verbose_name=_("YouTube Stream"),
    )
    sermons = models.ManyToManyField(
        Sermon,
        related_name="services",
        verbose_name=Sermon._meta.verbose_name_plural,
        blank=True,
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ["-datetime"]

    def __str__(self) -> str:
        return f"{self.datetime}"

    def html_youtube_link(self):
        if self.youtube_stream_id:
            return self.youtube_stream.html_object_link

    html_youtube_link.short_description = "YouTube Stream"
