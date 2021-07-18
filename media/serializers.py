# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import SoundCloudAsset, YouTubeAsset


class SoundCloudAssetSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail_url = serializers.FileField(source="overriden_thumbnail_field")

    class Meta:
        model = SoundCloudAsset
        fields = [
            "id",
            "url",
            "title",
            "object_id",
            "object_url",
            "oembed_object_url",
            "thumbnail_url",
            "track_id",
        ]


class YouTubeAssetSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail_url = serializers.FileField(source="overriden_thumbnail_field")

    class Meta:
        model = YouTubeAsset
        fields = [
            "id",
            "url",
            "title",
            "object_id",
            "object_url",
            "oembed_object_url",
            "thumbnail_url",
        ]
