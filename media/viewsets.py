# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import SoundCloudAssetFilterSet, YouTubeAssetFilterSet
from .models import SoundCloudAsset, YouTubeAsset
from .serializers import SoundCloudAssetSerializer, YouTubeAssetSerializer


class SoundCloudAssetViewSet(viewsets.ReadOnlyModelViewSet):
    model = SoundCloudAsset
    queryset = SoundCloudAsset.objects.all()
    serializer_class = SoundCloudAssetSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = SoundCloudAssetFilterSet


class YouTubeAssetViewSet(viewsets.ReadOnlyModelViewSet):
    model = YouTubeAsset
    queryset = YouTubeAsset.objects.all()
    serializer_class = YouTubeAssetSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = YouTubeAssetFilterSet
