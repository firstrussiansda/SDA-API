# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend
from utils.viewsets import SlugOrIdMixin

from .filtersets import PersonFilterSet
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(SlugOrIdMixin, viewsets.ReadOnlyModelViewSet):
    model = Person
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = Person.objects.all().order_by("name")
    serializer_class = PersonSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = PersonFilterSet
