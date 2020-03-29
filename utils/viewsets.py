# -*- coding: utf-8 -*-
import typing
from itertools import chain

from django.db import models
from rest_framework.exceptions import ValidationError


class OrderableMixin:
    orderable_fields: typing.List[str] = []
    default_order_field: typing.Optional[str] = None

    def get_orderable_fields(self) -> typing.Dict[str, str]:
        return {i: i for i in chain(*((i, f"-{i}") for i in self.orderable_fields))}

    def get_queryset_order_by(self) -> typing.List[str]:
        order_by = []
        orderable_fields = self.get_orderable_fields()
        for v in self.request.GET.getlist("order_by", []):
            try:
                order_by.append(orderable_fields[v])
            except KeyError:
                raise ValidationError({"order_by": f"{v} is not valid order_by field"})
        return [i for i in order_by or [self.default_order_field] if i]

    def get_queryset(self) -> models.QuerySet:
        qs = super().get_queryset()
        order_fields = self.get_queryset_order_by()
        if order_fields:
            qs = qs.order_by(*order_fields)
        return qs
