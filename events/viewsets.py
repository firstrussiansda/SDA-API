from rest_framework import viewsets

from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import EventFilterSet
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = EventFilterSet
