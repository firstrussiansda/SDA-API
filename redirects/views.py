# -*- coding: utf-8 -*-

from django.http import Http404
from django.views.generic import RedirectView
from services.models import Service


class ZoomMeetingRedirect(RedirectView):
    def get_redirect_url(self):
        service = (
            Service.objects.select_related("zoom_meeting")
            .exclude(zoom_meeting_id=None)
            .order_by("-datetime")
            .first()
        )
        if not service:
            raise Http404
        return service.zoom_meeting.zoom_link


class YouTubeServiceRedirect(RedirectView):
    def get_redirect_url(self):
        service = (
            Service.objects.select_related("youtube_stream")
            .exclude(youtube_stream_id=None)
            .order_by("-datetime")
            .first()
        )
        if not service:
            raise Http404
        return service.youtube_stream.object_url
