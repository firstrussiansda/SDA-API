# -*- coding: utf-8 -*-
from url_filter.constants import StrictMode
from url_filter.filtersets import ModelFilterSet

from .models import Person


class PersonFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    class Meta:
        model = Person
        fields = ["id", "name", "position"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in", "isnull"]},
            "name": {
                "lookups": [
                    "contains",
                    "endswith",
                    "exact",
                    "icontains",
                    "iendswith",
                    "iexact",
                    "in",
                    "iregex",
                    "istartswith",
                    "regex",
                ]
            },
            "position": {"lookups": ["exact", "iexact", "in", "isnull"]},
        }


class JustPersonFilterSet(PersonFilterSet):
    pass
