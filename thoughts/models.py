# -*- coding: utf-8 -*-
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel
from files.models import Attachment
from people.models import Person


class Thought(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True)
    thought_html = RichTextField(_("Thought"))

    date = models.DateField(_("Date"), null=True)

    authors = models.ManyToManyField(
        Person, related_name="thoughts", verbose_name=_("Authors"), blank=True
    )

    attachments = models.ManyToManyField(
        Attachment,
        related_name="thoughts",
        verbose_name=Attachment._meta.verbose_name_plural,
        blank=True,
    )

    class Meta:
        verbose_name = _("Thought")
        verbose_name_plural = _("Thoughts")

    def __str__(self):
        return f"{self.date} - {self.title}"