# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Attachment


class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            "id",
            "url",
            "name",
            "file",
        ]
