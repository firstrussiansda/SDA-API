# -*- coding: utf-8 -*-
from drf_yasg.inspectors.base import BaseInspector


class NoPaginationInspector(BaseInspector):
    def get_paginator_parameters(self, paginator):
        return []

    def get_paginated_response(self, paginator, response_schema):
        return response_schema
