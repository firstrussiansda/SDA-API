# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import SermonFilterSet, SermonSeriesFilterSet
from .models import Sermon, SermonSeries
from .serializers import (
    JustSermonSeriesSerializer,
    SermonSerializer,
    SermonSeriesSerializer,
)


class SermonSeriesViewSet(viewsets.ReadOnlyModelViewSet):
    model = SermonSeries
    queryset = SermonSeries.objects.all()
    serializer_class = SermonSeriesSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SermonSeriesFilterSet

    @property
    def is_sermons_expanded(self):
        return "sermons" in self.request.GET.getlist("expand", [])

    def get_serializer_class(self):
        if self.is_sermons_expanded:
            return super().get_serializer_class()
        else:
            return JustSermonSeriesSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.is_sermons_expanded:
            return qs.prefetch_related(
                "sermons",
                "sermons__speakers",
                "sermons__soundcloud_assets",
                "sermons__youtube_assets",
            ).all()
        return qs


class SermonViewSet(viewsets.ReadOnlyModelViewSet):
    model = Sermon
    queryset = (
        Sermon.objects.prefetch_related(
            "speakers", "soundcloud_assets", "youtube_assets"
        )
        .order_by("-date")
        .all()
    )
    serializer_class = SermonSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SermonFilterSet
