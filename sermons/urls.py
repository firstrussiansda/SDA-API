# -*- coding: utf-8 -*-
from rest_framework import routers

from .viewsets import SermonSeriesViewSet, SermonViewSet


router = type("Router", (routers.DefaultRouter,), {"include_root_view": False})()

router.register(r"series", SermonSeriesViewSet)
router.register(r"sermons", SermonViewSet)
