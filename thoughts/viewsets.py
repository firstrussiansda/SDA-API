# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend
from utils.viewsets import SlugOrIdMixin

from .filtersets import ThoughtFilterSet
from .models import Thought
from .serializers import ThoughtSerializer


class ThoughtViewSet(SlugOrIdMixin, viewsets.ReadOnlyModelViewSet):
    model = Thought
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    queryset = (
        Thought.objects.prefetch_related(
            "authors",
            "attachments",
        )
        .order_by("-date")
        .all()
    )
    serializer_class = ThoughtSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = ThoughtFilterSet
