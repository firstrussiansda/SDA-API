# -*- coding: utf-8 -*-
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("files", "0003_adding_attachments"),
        ("people", "0004_adding_person_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="Thought",
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
                (
                    "thought_html",
                    models.TextField(blank=True, null=True, verbose_name="Thought"),
                ),
                (
                    "thought_html_ru",
                    models.TextField(blank=True, null=True, verbose_name="Thought"),
                ),
                (
                    "thought_html_uk",
                    models.TextField(blank=True, null=True, verbose_name="Thought"),
                ),
                (
                    "thought_html_en",
                    models.TextField(blank=True, null=True, verbose_name="Thought"),
                ),
                ("date", models.DateField(null=True, verbose_name="Date")),
                (
                    "attachments",
                    models.ManyToManyField(
                        blank=True,
                        related_name="thoughts",
                        to="files.Attachment",
                        verbose_name="Attachments",
                    ),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        blank=True,
                        related_name="thoughts",
                        to="people.Person",
                        verbose_name="Authors",
                    ),
                ),
            ],
            options={"verbose_name": "Thought", "verbose_name_plural": "Thoughts"},
        ),
    ]
