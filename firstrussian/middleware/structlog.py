# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import typing

import structlog
from django.http import HttpRequest, HttpResponse


log = structlog.get_logger()


class StructLogMiddleware:
    def __init__(self, get_response: typing.Callable[..., HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        request.log = log.new()
        return self.get_response(request)
