# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0003_event_image_required")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="location_map_name",
            field=models.CharField(
                blank=True,
                help_text=(
                    "Location name to search in Google Maps. Should be unique to result"
                    " in single search result."
                ),
                max_length=255,
                verbose_name="Location Map Name",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="location_name_en",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Location Name"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="location_name_ru",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Location Name"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="location_name_uk",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Location Name"
            ),
        ),
    ]
