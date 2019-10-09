from rest_framework import routers

from .viewsets import SermonViewSet


router = type("Router", (routers.DefaultRouter,), {"include_root_view": False})()

router.register(r"sermons", SermonViewSet)
