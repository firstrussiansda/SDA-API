# -*- coding: utf-8 -*-
from functools import partial

from files.serializers import AttachmentSerializer
from rest_framework import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    serializer_url_field = partial(
        serializers.HyperlinkedIdentityField,
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )

    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Announcement
        fields = [
            "id",
            "url",
            "slug",
            "title",
            "description",
            "announcement_html",
            "is_featured",
            "alert_level",
            "start_date",
            "end_date",
            "attachments",
        ]
