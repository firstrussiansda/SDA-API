# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="location_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="Location Name"
            ),
        )
    ]
