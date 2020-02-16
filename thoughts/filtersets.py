# -*- coding: utf-8 -*-
from files.filtersets import AttachmentFilterSet
from people.filtersets import JustPersonFilterSet, PersonFilterSet
from url_filter.constants import StrictMode
from url_filter.filtersets import ModelFilterSet

from .models import Thought


class ThoughtFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    authors = JustPersonFilterSet()
    attachments = AttachmentFilterSet()

    class Meta:
        model = Thought
        fields = ["id", "slug", "title", "date"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in", "isnull"]},
            "slug": {
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
            "title": {
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
            "date": {
                "lookups": [
                    "day",
                    "exact",
                    "gt",
                    "gte",
                    "hour",
                    "in",
                    "lt",
                    "lte",
                    "minute",
                    "month",
                    "range",
                    "week_day",
                    "year",
                ]
            },
        }


# Inject sermons filter to people filterset
PersonFilterSet._declared_filters["thoughts"] = ThoughtFilterSet()
