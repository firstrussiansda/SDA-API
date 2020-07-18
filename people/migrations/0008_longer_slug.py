# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0007_unique_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text=(
                    "URL-friendly name. Can only be alphanumeric with hyphens as word"
                    " delimiter."
                ),
                max_length=128,
                unique=True,
                verbose_name="Slug",
            ),
        ),
    ]
