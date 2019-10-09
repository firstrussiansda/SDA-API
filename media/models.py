import re
import uuid
from urllib.parse import urlparse

from dirtyfields import DirtyFieldsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.http import QueryDict
from django.utils.http import urlquote
from django.utils.translation import gettext_lazy as _
from django_auxilium.models import BaseModel

from .utils import oembed_from_id


class BaseAsset(DirtyFieldsMixin, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    @property
    def object_url(self):
        return self.URL_PATTERN.format(**locals())

    @property
    def oembed_object_url(self):
        return self.OEMBED_URL_PATTERN.format(object_url=urlquote(self.object_url))

    @property
    def html_object_link(self):
        from django.utils.safestring import mark_safe

        return mark_safe(
            f'<a target="blank" href={self.object_url}>{self.object_url}</a>'
        )

    def clean(self):
        errors = {}
        for f in self.get_dirty_fields():
            if getattr(self, f):
                try:
                    getattr(self, f"clean_dirty_{f}")()
                except AttributeError:
                    continue
                except ValidationError as e:
                    errors.setdefault(f.name, []).append(e)
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.title


class SoundCloudAsset(BaseAsset):
    URL_PATTERN = "https://soundcloud.com/{self.object_id}"
    OEMBED_URL_PATTERN = "https://soundcloud.com/oembed?format=json&url={object_url}"

    title = models.CharField(_("Title"), max_length=128, editable=False)
    object_id = models.CharField(
        _("Object ID"),
        max_length=128,
        help_text="SoundCloud track ID. Can be given as full SoundCloud URL from which ID is extracted.",
    )
    thumbnail_url = models.URLField(_("Thumbnail URL"), max_length=256, editable=False)

    class Meta:
        verbose_name = _("SoundCloud Asset")
        verbose_name_plural = _("SoundCloud Assets")

    def clean_dirty_object_id(self):
        object_id = getattr(
            re.match(
                # match <username>/<slug> from path
                # for example /myaccount/testtrack -> myaccount/testtrack
                # but /myaccount/sets/playlist is invalid
                r"/?(?P<object_id>[^/]+/[^/?#]+)$",
                urlparse(self.object_id).path,
            ),
            "groupdict",
            dict,
        )().get("object_id")

        metadata = oembed_from_id(
            object_id,
            f"https://soundcloud.com/oembed?url=https://soundcloud.com/{object_id}&format=json",
            "SoundCloud",
            "Object ID",
            "<account>/<track-slug>",
        )
        self.object_id = metadata.object_id
        self.title = metadata.title
        self.thumbnail_url = metadata.thumbnail_url


class YouTubeAsset(BaseAsset):
    URL_PATTERN = "https://youtube.com/watch?v={self.object_id}"
    OEMBED_URL_PATTERN = "https://youtube.com/oembed?format=json&url={object_url}"

    title = models.CharField(_("Title"), max_length=128, editable=False)
    object_id = models.CharField(
        _("Object ID"),
        max_length=128,
        help_text="YouTube video ID. Can be given as full YouTube URL from which ID is extracted.",
    )
    thumbnail_url = models.URLField(_("Thumbnail URL"), max_length=256, editable=False)

    class Meta:
        verbose_name = _("YouTube Asset")
        verbose_name_plural = _("YouTube Assets")

    def clean_dirty_object_id(self):
        parsed = urlparse(self.object_id)
        if parsed.path == self.object_id:
            object_id = self.object_id
        else:
            object_id = QueryDict(urlparse(self.object_id).query).get("v")

        metadata = oembed_from_id(
            object_id,
            f"https://www.youtube.com/oembed?url=/watch?v={object_id}&format=json",
            "YouTube",
            "Object ID",
            "<video_id>",
        )
        self.object_id = metadata.object_id
        self.title = metadata.title
        self.thumbnail_url = metadata.thumbnail_url
