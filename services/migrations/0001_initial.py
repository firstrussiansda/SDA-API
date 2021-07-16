# -*- coding: utf-8 -*-
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("media", "0004_removing_default"),
        ("sermons", "0007_adding_sermon_is_published"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("datetime", models.DateTimeField(verbose_name="Time")),
                (
                    "sermons",
                    models.ManyToManyField(
                        blank=True,
                        related_name="services",
                        to="sermons.Sermon",
                        verbose_name="Sermons",
                    ),
                ),
                (
                    "youtube_stream",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="services",
                        to="media.YouTubeAsset",
                        verbose_name="YouTube Stream",
                    ),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
                "ordering": ["-datetime"],
            },
        ),
    ]
