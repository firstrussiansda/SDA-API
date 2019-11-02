# -*- coding: utf-8 -*-
import hashlib
import uuid

from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import (
    BaseModel,
    RandomImageField,
    file_field_auto_change_delete,
)


@file_field_auto_change_delete
class Person(DirtyFieldsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_("Name"), max_length=128)

    gravatar_email = models.EmailField(
        _("Email"), blank=True, help_text=_("Gravatar email for profile image")
    )
    profile_image = RandomImageField(
        _("Profile Image"),
        blank=True,
        upload_to="people/profiles_images",
        help_text=_("Uploaded profile image"),
    )

    position = models.CharField(
        _("Position"), max_length=128, blank=True, help_text=_("Position in the church")
    )
    about = models.TextField(_("About"), blank=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    @property
    def profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url
        if self.gravatar_email:
            email_hash = hashlib.md5(
                self.gravatar_email.encode("utf-8").lower().strip()
            ).hexdigest()
            return f"https://www.gravatar.com/avatar/{email_hash}?s=300"

    def __str__(self):
        return self.name
