# -*- coding: utf-8 -*-
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0006_adding_thumbnail_override"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZoomAsset",
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
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "zoom_link",
                    models.URLField(max_length=256, verbose_name="Zoom Link"),
                ),
            ],
            options={
                "verbose_name": "Zoom Asset",
                "verbose_name_plural": "Zoom Assets",
                "ordering": ["title"],
            },
        ),
        migrations.AlterModelOptions(
            name="soundcloudasset",
            options={
                "ordering": ["title"],
                "verbose_name": "SoundCloud Asset",
                "verbose_name_plural": "SoundCloud Assets",
            },
        ),
        migrations.AlterModelOptions(
            name="youtubeasset",
            options={
                "ordering": ["title", "start_at_seconds"],
                "verbose_name": "YouTube Asset",
                "verbose_name_plural": "YouTube Assets",
            },
        ),
    ]
