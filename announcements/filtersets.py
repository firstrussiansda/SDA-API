# -*- coding: utf-8 -*-
from files.filtersets import AttachmentFilterSet
from url_filter.constants import StrictMode
from url_filter.filtersets import ModelFilterSet

from .models import Announcement


class AnnouncementFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    attachments = AttachmentFilterSet()

    class Meta:
        model = Announcement
        fields = [
            "id",
            "slug",
            "title",
            "is_featured",
            "alert_level",
            "start_date",
            "end_date",
        ]
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
            "is_featured": {"lookups": ["exact"]},
            "alert_level": {"lookups": ["exact", "in"]},
            "start_date": {
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
            "end_date": {
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
