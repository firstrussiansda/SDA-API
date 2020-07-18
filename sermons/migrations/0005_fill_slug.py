# -*- coding: utf-8 -*-
from django.db import migrations
from django.utils.text import slugify


def fill_slug(apps, schema_editor) -> None:
    SermonSeries = apps.get_model("sermons", "SermonSeries")
    for sermon_series in SermonSeries.objects.all():
        sermon_series.slug = slugify(sermon_series.title_en or str(sermon_series.id))
        sermon_series.save()

    Sermon = apps.get_model("sermons", "Sermon")
    for sermon in Sermon.objects.all():
        sermon.slug = slugify(sermon.title_en or str(sermon.id))
        sermon.save()


class Migration(migrations.Migration):

    dependencies = [
        ("sermons", "0004_adding_slug"),
        ("sermons", "0004_longer_slug"),
    ]

    operations = [
        migrations.RunPython(fill_slug),
    ]
