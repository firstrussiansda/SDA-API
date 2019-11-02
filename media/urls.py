# -*- coding: utf-8 -*-
from rest_framework import routers

from .viewsets import SoundCloudAssetViewSet, YouTubeAssetViewSet


router = type("Router", (routers.DefaultRouter,), {"include_root_view": False})()

router.register(r"assets/soundcloud", SoundCloudAssetViewSet)
router.register(r"assets/youtube", YouTubeAssetViewSet)
