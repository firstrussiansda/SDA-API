# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0004_adding_person_about"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="person",
            options={
                "ordering": ["name"],
                "verbose_name": "Person",
                "verbose_name_plural": "People",
            },
        ),
        migrations.AddField(
            model_name="person",
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
