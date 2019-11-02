# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "url",
            "title",
            "description",
            "date",
            "is_featured",
            "image_url",
            "image_description",
            "location_name",
        ]
