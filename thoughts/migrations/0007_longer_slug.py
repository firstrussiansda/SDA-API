# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0006_bleach"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thought",
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
