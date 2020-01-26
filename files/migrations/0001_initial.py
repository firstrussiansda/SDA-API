# -*- coding: utf-8 -*-
import uuid

import dirtyfields.dirtyfields
import django_auxilium.models.fields.files
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attachment",
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
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                (
                    "file",
                    django_auxilium.models.fields.files.RandomFileField(
                        blank=True,
                        help_text="Attachment file",
                        upload_to="files/attachments",
                        verbose_name="File",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
