# -*- coding: utf-8 -*-
import uuid

from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel, RandomFileField


class Attachment(DirtyFieldsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_("Name"), max_length=128)
    file = RandomFileField(
        _("File"),
        blank=True,
        upload_to="files/attachments",
        help_text=_("Attachment file"),
    )

    class Meta:
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")

    def __str__(self):
        return self.name
