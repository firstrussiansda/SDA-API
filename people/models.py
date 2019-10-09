import hashlib
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_("Name"), max_length=128)

    gravatar_email = models.EmailField(
        _("Email"), blank=True, help_text=_("Gravatar email for profile image")
    )
    # TODO random path and delete hook
    profile_image = models.FileField(
        _("Profile Image"), blank=True, help_text=_("Uploaded profile image")
    )

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
