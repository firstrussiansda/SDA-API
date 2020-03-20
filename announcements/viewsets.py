# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import AnnouncementFilterSet
from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    model = Announcement
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = (
        Announcement.objects.prefetch_related("attachments")
        .order_by("start_date")
        .all()
    )
    serializer_class = AnnouncementSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = AnnouncementFilterSet

    def get_object(self) -> Announcement:
        try:
            return super().get_object()
        except Http404:
            self.lookup_field = "id"
            return super().get_object()
