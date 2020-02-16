# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0002_added_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="thought",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="Thought title as it will appear in the URL. Can only be alphanumeric with hyphens as word delimiter.",
                max_length=64,
                verbose_name="Slug",
            ),
        ),
    ]
