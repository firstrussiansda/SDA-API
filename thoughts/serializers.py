# -*- coding: utf-8 -*-
from functools import partial

from files.serializers import AttachmentSerializer
from people.serializers import PersonSerializer
from rest_framework import serializers

from .models import Thought


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    serializer_url_field = partial(
        serializers.HyperlinkedIdentityField,
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )

    authors = PersonSerializer(many=True)
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Thought
        fields = [
            "id",
            "url",
            "slug",
            "title",
            "description",
            "image_url",
            "image_description",
            "thought_html",
            "date",
            "authors",
            "attachments",
        ]
