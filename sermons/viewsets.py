# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import SermonFilterSet, SermonSeriesFilterSet
from .models import Sermon, SermonSeries
from .serializers import SermonSerializer, SermonSeriesSerializer


class SermonSeriesViewSet(viewsets.ReadOnlyModelViewSet):
    model = SermonSeries
    queryset = SermonSeries.objects.prefetch_related("sermons").all()
    serializer_class = SermonSeriesSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SermonSeriesFilterSet


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
