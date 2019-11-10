# -*- coding: utf-8 -*-
from media.filtersets import SoundCloudAssetFilterSet, YouTubeAssetFilterSet
from people.filtersets import PersonFilterSet
from url_filter.filtersets import ModelFilterSet

from .models import Sermon, SermonSeries


class JustPersonFilterSet(PersonFilterSet):
    pass


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


class JustSermonSpeakerFilterSet(JustSermonFilterSet):
    speakers = JustPersonFilterSet()


class SermonSeriesFilterSet(JustSermonSeriesFilterSet):
    sermons = JustSermonSpeakerFilterSet()


class SermonFilterSet(JustSermonSpeakerFilterSet):
    series = JustSermonSeriesFilterSet()


class SermonNoSpeakerFilterSet(JustSermonFilterSet):
    series = JustSermonSeriesFilterSet()


# Inject sermons filter to people filterset
PersonFilterSet._declared_filters["sermons"] = SermonNoSpeakerFilterSet()
