# -*- coding: utf-8 -*-
from django.urls import path

from .views import YouTubeServiceRedirect, ZoomMeetingRedirect


urlpatterns = [
    # apis in root
    path("youtube", YouTubeServiceRedirect.as_view()),
    path("zoom", ZoomMeetingRedirect.as_view()),
]
