# -*- coding: utf-8 -*-
import operator
from functools import reduce

from django.conf import settings
from django.db import models
from modeltranslation.manager import (
    MultilingualQuerySet,
    get_translatable_fields_for_model,
)


class MultilingualFilterQuerySet(MultilingualQuerySet):
    def _filter_or_exclude(self, negate, *args, **kwargs):
        more_args = []
        translatable = get_translatable_fields_for_model(self.model)

        for key, value in list(kwargs.items()):
            field, *lookups = key.split("__")
            if field in translatable:
                del kwargs[key]
                more_args.append(
                    reduce(
                        operator.or_,
                        (
                            models.Q(**{"__".join([f"{field}_{i}"] + lookups): value})
                            for i in (i[0] for i in settings.LANGUAGES)
                        ),
                    )
                )

        return super()._filter_or_exclude(negate, *(args + tuple(more_args)), **kwargs)
