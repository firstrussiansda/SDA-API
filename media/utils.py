import re
from dataclasses import dataclass

import requests
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from structlog import get_logger


log = get_logger()


@dataclass
class OEmbedData:
    object_id: str
    title: str
    thumbnail_url: str
    html: str


def oembed_from_id(object_id, oembed_url, service, field, pattern):
    if not object_id:
        raise ValidationError(
            _("This field does match expected pattern %(pattern)s.") % locals()
        )

    log_kwargs = {"service": service, "field": field, "url": oembed_url}

    try:
        r = requests.get(oembed_url)
    except requests.RequestException as e:
        log.exception("Could not connect to external oembed service", **log_kwargs)
        raise ValidationError(
            _("Could not connect to %(service)s to validate %(field)s.") % locals()
        ) from e

    if r.status_code == 404:
        raise ValidationError(_("%(service)s %(field)s not found.") % locals())

    elif r.status_code != 200:
        log.error("Received error from external oembed", **log_kwargs)
        raise ValidationError(
            _("Could not validate %(field)s due to %(service)s error.") % locals()
        )

    try:
        data = r.json()
    except ValueError as e:
        log.exception(
            "Received invalid json response from external oembed", **log_kwargs
        )
        raise ValidationError(
            _("Could not validate %(field)s due to invalid response from %(service)s.")
            % locals()
        ) from e

    return OEmbedData(
        object_id=object_id,
        title=data.get("title"),
        thumbnail_url=data.get("thumbnail_url"),
        html=data.get("html"),
    )
