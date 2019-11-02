# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import SoundCloudAsset, YouTubeAsset


class SoundCloudAssetSerializer(serializers.HyperlinkedModelSerializer):
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
