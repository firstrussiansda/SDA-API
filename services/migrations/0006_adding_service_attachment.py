# -*- coding: utf-8 -*-
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0007_ordcering_attachment"),
        ("services", "0005_adding_zoom_meeting"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceAttachment",
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
                ("notes", models.TextField(blank=True, verbose_name="Notes")),
                (
                    "attachment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="files.Attachment",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.Service",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="service",
            name="attachments",
            field=models.ManyToManyField(
                through="services.ServiceAttachment",
                to="files.Attachment",
                verbose_name="Attachments",
            ),
        ),
    ]
