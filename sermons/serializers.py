# -*- coding: utf-8 -*-
from files.serializers import AttachmentSerializer
from media.serializers import SoundCloudAssetSerializer, YouTubeAssetSerializer
from people.serializers import PersonSerializer
from rest_framework import serializers

from .models import Sermon, SermonSeries


class JustSermonSeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SermonSeries
        fields = ["id", "url", "title", "description"]


class JustSermonSerializer(serializers.HyperlinkedModelSerializer):
    speakers = PersonSerializer(many=True)
    soundcloud_assets = SoundCloudAssetSerializer(many=True)
    youtube_assets = YouTubeAssetSerializer(many=True)
    attachments = AttachmentSerializer(many=True)

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
            "attachments",
        ]


class SermonSeriesSerializer(JustSermonSeriesSerializer):
    sermons = JustSermonSerializer(many=True)

    class Meta(JustSermonSeriesSerializer.Meta):
        fields = JustSermonSeriesSerializer.Meta.fields + ["sermons"]


class SermonSerializer(JustSermonSerializer):
    series = JustSermonSeriesSerializer()

    class Meta(JustSermonSerializer.Meta):
        fields = JustSermonSerializer.Meta.fields + ["series"]


class SermonYearMonthsSerializer(serializers.Serializer):
    year = serializers.DictField(child=serializers.IntegerField())
