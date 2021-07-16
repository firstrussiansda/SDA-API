# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("media", "0003_adding_track_id")]

    operations = [
        migrations.AlterField(
            model_name="soundcloudasset",
            name="track_id",
            field=models.CharField(
                editable=False,
                help_text="SoundCloud track ID. Extracted from a linked SoundCloud resource.",
                max_length=32,
                verbose_name="Track ID",
            ),
        )
    ]
