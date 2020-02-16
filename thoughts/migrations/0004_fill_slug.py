# -*- coding: utf-8 -*-
from django.db import migrations
from django.utils.text import slugify


def fill_slug(apps, schema_editor) -> None:
    Thought = apps.get_model("thoughts", "Thought")
    for thought in Thought.objects.all():
        thought.slug = slugify(thought.title_en or str(thought.id))
        thought.save()


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0003_adding_slug"),
    ]

    operations = [
        migrations.RunPython(fill_slug),
    ]
