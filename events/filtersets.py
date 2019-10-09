from url_filter.filtersets import ModelFilterSet

from .models import Event


class EventFilterSet(ModelFilterSet):
    class Meta:
        model = Event
        fields = ["id", "date", "is_featured"]
        extra_kwargs = {
            "id": {"lookups": ["exact", "in"]},
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
            "is_featured": {"lookups": ["exact"]},
        }
