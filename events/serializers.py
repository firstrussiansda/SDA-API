# -*- coding: utf-8 -*-
from files.serializers import AttachmentSerializer
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    attachments = AttachmentSerializer(many=True)

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
            "location_map_name",
            "location_google_maps_url",
            "attachments",
        ]
