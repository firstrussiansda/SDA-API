from rest_framework import viewsets

from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import PersonFilterSet
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = PersonFilterSet
