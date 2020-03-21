# -*- coding: utf-8 -*-
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("files", "0003_adding_attachments"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="Announcement title as it will appear in the URL. Can only be alphanumeric with hyphens as word delimiter.",
                        max_length=64,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_uk",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_uk",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="Is Featured"),
                ),
                (
                    "alert_level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("INFO", "Info"),
                            ("WARNING", "Warning"),
                            ("DANGER", "Danger"),
                        ],
                        max_length=8,
                        verbose_name="Alert Level",
                    ),
                ),
                ("start_date", models.DateField(null=True, verbose_name="Start Date")),
                ("end_date", models.DateField(null=True, verbose_name="End Date")),
                (
                    "image_url",
                    models.URLField(
                        help_text="You can find many free images at unsplash.com",
                        max_length=512,
                        verbose_name="Image URL",
                    ),
                ),
                (
                    "image_description",
                    models.CharField(
                        blank=True, max_length=512, verbose_name="Image Description"
                    ),
                ),
                (
                    "attachments",
                    models.ManyToManyField(
                        blank=True,
                        related_name="announcements",
                        to="files.Attachment",
                        verbose_name="Attachments",
                    ),
                ),
            ],
            options={
                "verbose_name": "Announcement",
                "verbose_name_plural": "Announcements",
            },
        ),
    ]
