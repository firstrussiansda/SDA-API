# -*- coding: utf-8 -*-
import uuid

from dirtyfields import DirtyFieldsMixin
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.templatetags.l10n import localize
from django.utils.timezone import localtime, now
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from media.models import YouTubeAsset, ZoomAsset
from sermons.models import Sermon
from structlog import get_logger
from utils.models import BleachRichTextField


log = get_logger()


class Service(DirtyFieldsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    datetime = models.DateTimeField(_("Time"), null=False)

    program_html = BleachRichTextField(_("Program"), blank=True)

    subscribers = models.ManyToManyField(
        get_user_model(),
        related_name="services",
        verbose_name=_("Subscribers"),
        blank=True,
    )

    zoom_meeting = models.ForeignKey(
        ZoomAsset,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="services",
        verbose_name=_("Zoom Meeting"),
    )
    youtube_stream = models.ForeignKey(
        YouTubeAsset,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="services",
        verbose_name=_("YouTube Stream"),
    )
    sermons = models.ManyToManyField(
        Sermon,
        related_name="services",
        verbose_name=Sermon._meta.verbose_name_plural,
        blank=True,
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ["-datetime"]

    def __str__(self) -> str:
        return f"{self.datetime.strftime('%A')} {localize(localtime(self.datetime))}"

    def html_youtube_link(self):
        if self.youtube_stream_id:
            return self.youtube_stream.html_object_link

    html_youtube_link.short_description = "YouTube Stream"

    def html_zoom_link(self):
        if self.zoom_meeting_id:
            return self.zoom_meeting.zoom_link_html

    html_zoom_link.short_description = "Zoom Meeting Link"


@receiver(models.signals.post_save, sender=Service)
def handle_service_change(sender, instance: Service, created, **kwargs):
    if now() > instance.datetime:
        return
    if not created and not any(
        i in instance.get_dirty_fields() for i in ["program_html", "youtube_stream_id"]
    ):
        return

    for person in instance.subscribers.exclude(email=None):
        log.info(
            "Sending service notification email",
            to_email=person.email,
        )
        send_mail(
            subject=f"Service {instance} has changed",
            message="only html message is supported",
            html_message=f"""
<h1>{'Created' if created else 'Updated'} Service</h1>
<hr>
<h2>About Service</h2>
<p>Time: <strong>{instance}</strong></p>
<p>YouTube Stream: <strong>{instance.youtube_stream.html_object_link if instance.youtube_stream_id else 'none'}</strong></p>
<hr>
<h2>Service Program</h2>
{instance.program_html}
""",
            from_email=settings.EMAIL_NOTIFICATIONS,
            recipient_list=[person.email],
        )
