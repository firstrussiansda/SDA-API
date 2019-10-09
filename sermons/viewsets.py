from rest_framework import viewsets

from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import SermonFilterSet
from .models import Sermon
from .serializers import SermonSerializer


class SermonViewSet(viewsets.ReadOnlyModelViewSet):
    model = Sermon
    queryset = Sermon.objects.prefetch_related(
        "speakers", "soundcloud_assets", "youtube_assets"
    ).all()
    serializer_class = SermonSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SermonFilterSet
