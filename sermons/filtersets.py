# -*- coding: utf-8 -*-
from files.filtersets import AttachmentFilterSet
from media.filtersets import SoundCloudAssetFilterSet, YouTubeAssetFilterSet
from people.filtersets import JustPersonFilterSet, PersonFilterSet
from url_filter.constants import StrictMode
from url_filter.filtersets import ModelFilterSet

from .models import Sermon, SermonSeries


class JustSermonSeriesFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    class Meta:
        model = SermonSeries
        fields = ["id", "slug", "title"]
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
        }


class JustSermonFilterSet(ModelFilterSet):
    default_strict_mode = StrictMode.fail

    soundcloud_assets = SoundCloudAssetFilterSet()
    youtube_assets = YouTubeAssetFilterSet()
    attachments = AttachmentFilterSet()

    class Meta:
        model = Sermon
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
