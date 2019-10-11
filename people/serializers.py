from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    profile_image_url = serializers.SerializerMethodField("get_profile_image_url")

    class Meta:
        model = Person
        fields = ["id", "url", "name", "profile_image_url", "position"]

    def get_profile_image_url(self, obj):
        url = obj.profile_image_url
        if url and self.context.get("request"):
            return self.context.get("request").build_absolute_uri(url)
