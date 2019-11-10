# -*- coding: utf-8 -*-
import typing
import uuid
from collections import defaultdict

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from media.models import SoundCloudAsset, YouTubeAsset
from people.models import Person


class SermonSeries(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Sermon Series")
        verbose_name_plural = _("Sermon Series")

    def __str__(self):
        return f"{self.title}"


class SermonAggregateManager(models.Manager):
    def all_year_months(self) -> typing.Dict[int, typing.Dict[int, int]]:
        results = (
            self.get_queryset()
            .values("date__year", "date__month")
            .annotate(models.Count("date__month"))
        )
        data: typing.Dict[int, typing.Dict[int, int]] = defaultdict(
            lambda: {i: 0 for i in range(1, 13)}
        )
        for i in results:
            data[i["date__year"]][i["date__month"]] = i["date__month__count"]
        return dict(sorted(data.items()))


class Sermon(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True)

    date = models.DateField(_("Date"), null=True)

    series = models.ForeignKey(
        SermonSeries,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sermons",
        verbose_name=_("Series"),
    )

    speakers = models.ManyToManyField(
        Person, related_name="sermons", verbose_name=_("Speakers"), blank=True
    )

    # assets
    soundcloud_assets = models.ManyToManyField(
        SoundCloudAsset,
        related_name="sermons",
        verbose_name=SoundCloudAsset._meta.verbose_name_plural,
        blank=True,
    )
    youtube_assets = models.ManyToManyField(
        YouTubeAsset,
        related_name="sermons",
        verbose_name=YouTubeAsset._meta.verbose_name_plural,
        blank=True,
    )

    objects = SermonAggregateManager()

    class Meta:
        verbose_name = _("Sermon")
        verbose_name_plural = _("Sermons")

    def __str__(self):
        return f"{self.date} - {self.title}"
