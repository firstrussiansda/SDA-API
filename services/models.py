# -*- coding: utf-8 -*-
import typing
import uuid

from dirtyfields import DirtyFieldsMixin
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.templatetags.l10n import localize
from django.utils.html import strip_tags
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

    def send_email_to(self, *, to: User, created: bool = False):
        if now() > self.datetime:
            return
        log.info(
            "Sending service notification email",
            to_email=to.email,
        )
        context = {
            "to": to,
            "service": self,
            "created": created,
        }
        subject = render_to_string(
            "services/service_change_subject.txt", context
        ).strip()
        html_message = render_to_string("services/service_change_body.html", context)
        txt_message = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=txt_message,
            html_message=html_message,
            from_email=settings.EMAIL_NOTIFICATIONS,
            recipient_list=[to.email],
        )


@receiver(models.signals.post_save, sender=Service)
def handle_service_change(sender, instance: Service, created, **kwargs):
    for person in instance.subscribers.exclude(email=None):
        instance.send_email_to(to=person, created=created)


@receiver(models.signals.m2m_changed, sender=Service.subscribers.through)
def handle_service_subscriber_create(
    sender,
    instance: Service,
    action: str,
    reverse: bool,
    model,
    pk_set: typing.Set[uuid.UUID],
    **kwargs,
):
    if reverse:
        return
    if action != "post_add":
        return
    users = model.objects.filter(pk__in=pk_set)
    for user in users:
        instance.send_email_to(to=user, created=True)
