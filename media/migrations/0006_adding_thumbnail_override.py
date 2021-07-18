# -*- coding: utf-8 -*-
import django_auxilium.models.fields.files
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0005_youtube_start_at_seconds"),
    ]

    operations = [
        migrations.AddField(
            model_name="soundcloudasset",
            name="thumbnail_override",
            field=django_auxilium.models.fields.files.RandomFileField(
                blank=True,
                help_text="Override thumbnail from soundcloud",
                upload_to="media/soundcloud-thumbnails",
                verbose_name="Thumbnail Override",
            ),
        ),
        migrations.AddField(
            model_name="youtubeasset",
            name="thumbnail_override",
            field=django_auxilium.models.fields.files.RandomFileField(
                blank=True,
                help_text="Override thumbnail from YouTube",
                upload_to="media/youtube-thumbnails",
                verbose_name="Thumbnail Override",
            ),
        ),
    ]
