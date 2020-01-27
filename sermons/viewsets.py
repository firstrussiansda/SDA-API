# -*- coding: utf-8 -*-
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend
from utils.drf_yasg import NoPaginationInspector

from .filtersets import SermonFilterSet, SermonSeriesFilterSet
from .models import Sermon, SermonSeries
from .serializers import (
    JustSermonSeriesSerializer,
    SermonSerializer,
    SermonSeriesSerializer,
    SermonYearMonthsSerializer,
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
                "sermons__attachments",
            ).all()
        return qs


class SermonViewSet(viewsets.ReadOnlyModelViewSet):
    model = Sermon
    queryset = (
        Sermon.objects.prefetch_related(
            "speakers", "soundcloud_assets", "youtube_assets", "attachments",
        )
        .order_by("-date")
        .all()
    )
    serializer_class = SermonSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SermonFilterSet

    @swagger_auto_schema(
        paginator_inspectors=[NoPaginationInspector],
        responses={
            200: openapi.Response(
                "Get count of sermons for specific year and month",
                SermonYearMonthsSerializer,
            )
        },
    )
    @action(detail=False, url_path="year-months")
    def year_months(self, request, *args, **kwargs):
        return Response(
            self.filter_queryset(Sermon.objects.with_year_months()).all_year_months()
        )
