# -*- coding: utf-8 -*-
from rest_framework import routers

from .viewsets import AttachmentViewSet


router = type("Router", (routers.DefaultRouter,), {"include_root_view": False})()

router.register(r"files/attachments", AttachmentViewSet)
