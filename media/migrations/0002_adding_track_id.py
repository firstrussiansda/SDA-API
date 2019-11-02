# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("media", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="soundcloudasset",
            name="track_id",
            field=models.CharField(
                help_text="SoundCloud track ID. Extracted from a linked SoundCloud resource.",
                max_length=32,
                editable=False,
                verbose_name="Object ID",
                default="",
            ),
        ),
        migrations.AlterField(
            model_name="soundcloudasset",
            name="object_id",
            field=models.CharField(
                help_text="SoundCloud object ID. Can be given as full SoundCloud URL from which ID is extracted.",
                max_length=128,
                verbose_name="Object ID",
            ),
        ),
    ]
