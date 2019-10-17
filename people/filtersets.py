from url_filter.filtersets import ModelFilterSet

from .models import Person


class PersonFilterSet(ModelFilterSet):
    class Meta:
        model = Person
        fields = ["id", "name", "position"]
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
            "position": {"lookups": ["exact", "iexact", "in", "isnull"]},
        }
