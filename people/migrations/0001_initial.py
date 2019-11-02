# -*- coding: utf-8 -*-
import uuid

import django_auxilium.models.fields.files
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
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
                    "name_ru",
                    models.CharField(max_length=128, null=True, verbose_name="Name"),
                ),
                (
                    "name_uk",
                    models.CharField(max_length=128, null=True, verbose_name="Name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=128, null=True, verbose_name="Name"),
                ),
                (
                    "gravatar_email",
                    models.EmailField(
                        blank=True,
                        help_text="Gravatar email for profile image",
                        max_length=254,
                        verbose_name="Email",
                    ),
                ),
                (
                    "profile_image",
                    django_auxilium.models.fields.files.RandomImageField(
                        blank=True,
                        help_text="Uploaded profile image",
                        upload_to="people/profiles_images",
                        verbose_name="Profile Image",
                    ),
                ),
            ],
            options={"verbose_name": "Person", "verbose_name_plural": "People"},
        )
    ]
