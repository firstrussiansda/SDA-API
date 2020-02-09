# -*- coding: utf-8 -*-
import typing
from urllib.parse import urlparse, urlunparse


def remove_querystring(url: str, hostname: str = None) -> str:
    parsed = urlparse(url)
    if hostname and not parsed.hostname.endswith(hostname):
        return url
    kwargs = {**parsed._asdict(), **{"query": ""}}
    return typing.cast(str, urlunparse(kwargs.values()))
