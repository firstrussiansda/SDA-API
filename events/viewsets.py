# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import action
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend
from utils.viewsets import OrderableMixin

from .filtersets import EventFilterSet
from .models import Event
from .serializers import EventSerializer


class EventViewSet(OrderableMixin, viewsets.ReadOnlyModelViewSet):
    model = Event
    queryset = Event.objects.prefetch_related("attachments").all()
    serializer_class = EventSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = EventFilterSet
    orderable_fields = ["is_featured", "date"]
    default_order_field = "date"

    @action(detail=False)
    def featured(self, request, *args, **kwargs):
        self.queryset = self.__class__.queryset.order_by("-is_featured", "date")
        return self.list(request, *args, **kwargs)
