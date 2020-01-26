# -*- coding: utf-8 -*-
from rest_framework import viewsets
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend

from .filtersets import AttachmentFilterSet
from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ReadOnlyModelViewSet):
    model = Attachment
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    filter_backends = [CoreAPIURLFilterBackend]
    filter_class = AttachmentFilterSet
