# -*- coding: utf-8 -*-
from functools import partial

from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    serializer_url_field = partial(
        serializers.HyperlinkedIdentityField,
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )
    profile_image_url = serializers.SerializerMethodField("get_profile_image_url")

    class Meta:
        model = Person
        fields = ["id", "url", "slug", "name", "profile_image_url", "position", "about"]

    def get_profile_image_url(self, obj):
        url = obj.profile_image_url
        if url and self.context.get("request"):
            return self.context.get("request").build_absolute_uri(url)
