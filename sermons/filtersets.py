from media.filtersets import SoundCloudAssetFilterSet, YouTubeAssetFilterSet
from people.filtersets import PersonFilterSet
from url_filter.filtersets import ModelFilterSet

from .models import Sermon


class SermonFilterSet(ModelFilterSet):
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
