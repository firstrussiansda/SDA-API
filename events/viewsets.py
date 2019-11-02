# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import action
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import EventFilterSet
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    model = Event
    queryset = Event.objects.order_by("date").all()
    serializer_class = EventSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = EventFilterSet

    @action(detail=False)
    def featured(self, request, *args, **kwargs):
        self.queryset = self.__class__.queryset.order_by("-is_featured", "date")
        return self.list(request, *args, **kwargs)
