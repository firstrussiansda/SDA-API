# -*- coding: utf-8 -*-
from url_filter.filtersets import ModelFilterSet

from .models import SoundCloudAsset, YouTubeAsset


class SoundCloudAssetFilterSet(ModelFilterSet):
    class Meta:
        model = SoundCloudAsset
        fields = ["id", "title"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in"]},
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
        }


class YouTubeAssetFilterSet(ModelFilterSet):
    class Meta:
        model = YouTubeAsset
        fields = ["id", "title"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in"]},
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
        }
