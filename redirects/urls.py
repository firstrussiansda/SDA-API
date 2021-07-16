# -*- coding: utf-8 -*-
from django.urls import path

from .views import YouTubeServiceRedirect


urlpatterns = [
    # apis in root
    path("youtube", YouTubeServiceRedirect.as_view()),
]
