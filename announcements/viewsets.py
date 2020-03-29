# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend
from utils.viewsets import OrderableMixin

from .filtersets import AnnouncementFilterSet
from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementViewSet(OrderableMixin, viewsets.ReadOnlyModelViewSet):
    model = Announcement
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = Announcement.objects.prefetch_related("attachments").all()
    serializer_class = AnnouncementSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = AnnouncementFilterSet
    orderable_fields = ["start_date", "is_featured", "alert_level"]
    default_order_field = "start_date"

    def get_object(self) -> Announcement:
        try:
            return super().get_object()
        except Http404:
            self.lookup_field = "id"
            return super().get_object()
