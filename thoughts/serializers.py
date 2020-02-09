# -*- coding: utf-8 -*-
from files.serializers import AttachmentSerializer
from people.serializers import PersonSerializer
from rest_framework import serializers

from .models import Thought


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    authors = PersonSerializer(many=True)
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Thought
        fields = [
            "id",
            "url",
            "title",
            "description",
            "image_url",
            "image_description",
            "thought_html",
            "date",
            "authors",
            "attachments",
        ]
