# -*- coding: utf-8 -*-
from media.serializers import SoundCloudAssetSerializer, YouTubeAssetSerializer
from people.serializers import PersonSerializer
from rest_framework import serializers

from .models import Sermon


class SermonSerializer(serializers.HyperlinkedModelSerializer):
    speakers = PersonSerializer(many=True)
    soundcloud_assets = SoundCloudAssetSerializer(many=True)
    youtube_assets = YouTubeAssetSerializer(many=True)

    class Meta:
        model = Sermon
        fields = [
            "id",
            "url",
            "title",
            "description",
            "date",
            "speakers",
            "soundcloud_assets",
            "youtube_assets",
        ]
