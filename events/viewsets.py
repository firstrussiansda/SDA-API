# -*- coding: utf-8 -*-
import typing
from itertools import chain

from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import EventFilterSet
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    model = Event
    queryset = Event.objects.prefetch_related("attachments").all()
    serializer_class = EventSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = EventFilterSet
    orderable_fields = {
        i: i for i in chain(*((i, f"-{i}") for i in ("is_featured", "date",)))
    }

    def get_queryset_order_by(self) -> typing.List[str]:
        order_by = []
        for v in self.request.GET.getlist("order_by", []):
            try:
                order_by.append(self.orderable_fields[v])
            except KeyError:
                raise ValidationError({"order_by": f"{v} is not valid order_by field"})
        return order_by or ["date"]

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by(*self.get_queryset_order_by())

    @action(detail=False)
    def featured(self, request, *args, **kwargs):
        self.queryset = self.__class__.queryset.order_by("-is_featured", "date")
        return self.list(request, *args, **kwargs)
