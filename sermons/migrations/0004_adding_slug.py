# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sermons", "0003_adding_attachments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sermon",
            options={
                "ordering": ["-date"],
                "verbose_name": "Sermon",
                "verbose_name_plural": "Sermons",
            },
        ),
        migrations.AlterModelOptions(
            name="sermonseries",
            options={
                "ordering": ["title"],
                "verbose_name": "Sermon Series",
                "verbose_name_plural": "Sermon Series",
            },
        ),
        migrations.AddField(
            model_name="sermon",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text=(
                    "URL-friendly name. Can only be alphanumeric with hyphens as word"
                    " delimiter."
                ),
                max_length=64,
                verbose_name="Slug",
            ),
        ),
        migrations.AddField(
            model_name="sermonseries",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text=(
                    "URL-friendly name. Can only be alphanumeric with hyphens as word"
                    " delimiter."
                ),
                max_length=64,
                verbose_name="Slug",
            ),
        ),
    ]
