# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sermons", "0005_fill_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sermon",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text=(
                    "URL-friendly name. Can only be alphanumeric with hyphens as word"
                    " delimiter."
                ),
                max_length=64,
                unique=True,
                verbose_name="Slug",
            ),
        ),
        migrations.AlterField(
            model_name="sermonseries",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text=(
                    "URL-friendly name. Can only be alphanumeric with hyphens as word"
                    " delimiter."
                ),
                max_length=64,
                unique=True,
                verbose_name="Slug",
            ),
        ),
    ]
