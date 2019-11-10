# -*- coding: utf-8 -*-
from media.filtersets import SoundCloudAssetFilterSet, YouTubeAssetFilterSet
from people.filtersets import PersonFilterSet
from url_filter.filtersets import ModelFilterSet

from .models import Sermon, SermonSeries


class JustSermonSeriesFilterSet(ModelFilterSet):
    class Meta:
        model = SermonSeries
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


class JustSermonFilterSet(ModelFilterSet):
    speakers = PersonFilterSet()
    soundcloud_assets = SoundCloudAssetFilterSet()
    youtube_assets = YouTubeAssetFilterSet()

    class Meta:
        model = Sermon
        fields = ["id", "title", "date"]
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


class SermonSeriesFilterSet(JustSermonSeriesFilterSet):
    sermons = JustSermonFilterSet()


class SermonFilterSet(JustSermonFilterSet):
    series = JustSermonSeriesFilterSet()


# Inject sermons filter to people filterset


class SermonForPeopleFilterSet(ModelFilterSet):
    class Meta:
        model = Sermon
        fields = ["id"]
        extra_kwargs = {
            "id": {"lookups": ["isnull"]},
        }


PersonFilterSet._declared_filters["sermons"] = SermonForPeopleFilterSet()
