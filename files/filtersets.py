# -*- coding: utf-8 -*-
from url_filter.constants import StrictMode
from url_filter.filtersets import ModelFilterSet

from .models import Attachment


class AttachmentFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    class Meta:
        model = Attachment
        fields = ["id", "name", "file"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in"]},
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
        }
