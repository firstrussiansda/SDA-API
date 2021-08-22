# -*- coding: utf-8 -*-
import hashlib
import uuid

from dirtyfields import DirtyFieldsMixin
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel, RandomFileField


class Attachment(DirtyFieldsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_("Name"), max_length=128)
    file = RandomFileField(
        _("File"),
        blank=False,
        upload_to="files/attachments",
        help_text=_("Attachment file"),
    )
    checksum = models.CharField(
        _("Checksum"),
        unique=True,
        max_length=64,
        null=False,
    )

    class Meta:
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")
        ordering = ["-created"]

    def __str__(self):
        return self.name

    def validate_unique(self, exclude=None):
        exclude = [i for i in exclude if i not in ["checksum"]] if exclude else None
        try:
            super().validate_unique(exclude=exclude)
        except ValidationError as e:
            if "checksum" in e.error_dict:
                e.error_dict.setdefault(NON_FIELD_ERRORS, []).extend(
                    e.error_dict.pop("checksum")
                )
            raise e

    def clean(self) -> None:
        self.clean_checksum()
        super().clean()

    def clean_checksum(self) -> None:
        if not self.checksum:
            if self.file.closed:
                with self.file.open("rb") as fid:
                    self.checksum = hashlib.sha256(fid.read()).hexdigest()
            else:
                position = self.file.tell()
                try:
                    self.file.seek(0)
                    self.checksum = hashlib.sha256(self.file.read()).hexdigest()
                finally:
                    self.file.seek(position)
