# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import ThoughtFilterSet
from .models import Thought
from .serializers import ThoughtSerializer


class ThoughtViewSet(viewsets.ReadOnlyModelViewSet):
    model = Thought
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = (
        Thought.objects.prefetch_related("authors", "attachments",)
        .order_by("-date")
        .all()
    )
    serializer_class = ThoughtSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = ThoughtFilterSet

    def get_object(self) -> Thought:
        try:
            return super().get_object()
        except Http404:
            self.lookup_field = "id"
            return super().get_object()
