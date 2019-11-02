# -*- coding: utf-8 -*-
from rest_framework import routers

from .viewsets import PersonViewSet


router = type("Router", (routers.DefaultRouter,), {"include_root_view": False})()

router.register(r"people", PersonViewSet)
