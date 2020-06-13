# -*- coding: utf-8 -*-
import uuid

import dirtyfields.dirtyfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SoundCloudAsset",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        editable=False, max_length=128, verbose_name="Title"
                    ),
                ),
                (
                    "object_id",
                    models.CharField(
                        help_text=(
                            "SoundCloud track ID. Can be given as full SoundCloud URL"
                            " from which ID is extracted."
                        ),
                        max_length=128,
                        verbose_name="Object ID",
                    ),
                ),
                (
                    "thumbnail_url",
                    models.URLField(
                        editable=False, max_length=256, verbose_name="Thumbnail URL"
                    ),
                ),
            ],
            options={
                "verbose_name": "SoundCloud Asset",
                "verbose_name_plural": "SoundCloud Assets",
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name="YouTubeAsset",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        editable=False, max_length=128, verbose_name="Title"
                    ),
                ),
                (
                    "object_id",
                    models.CharField(
                        help_text=(
                            "YouTube video ID. Can be given as full YouTube URL from"
                            " which ID is extracted."
                        ),
                        max_length=128,
                        verbose_name="Object ID",
                    ),
                ),
                (
                    "thumbnail_url",
                    models.URLField(
                        editable=False, max_length=256, verbose_name="Thumbnail URL"
                    ),
                ),
            ],
            options={
                "verbose_name": "YouTube Asset",
                "verbose_name_plural": "YouTube Assets",
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
