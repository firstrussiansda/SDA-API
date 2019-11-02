# -*- coding: utf-8 -*-
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sermons", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="SermonSeries",
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
            ],
            options={
                "verbose_name": "Sermon Series",
                "verbose_name_plural": "Sermon Series",
            },
        ),
        migrations.AddField(
            model_name="sermon",
            name="series",
            field=models.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sermons",
                to="sermons.SermonSeries",
                verbose_name="Series",
            ),
        ),
    ]
