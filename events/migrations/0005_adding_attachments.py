# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_adding_attachments"),
        ("events", "0004_event_location_map_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="attachments",
            field=models.ManyToManyField(
                blank=True,
                related_name="events",
                to="files.Attachment",
                verbose_name="Attachments",
            ),
        ),
    ]
