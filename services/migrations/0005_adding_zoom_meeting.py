# -*- coding: utf-8 -*-
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0007_adding_zoom_asset"),
        ("services", "0004_adding_subscribers_backed_by_auth_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="zoom_meeting",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="services",
                to="media.ZoomAsset",
                verbose_name="Zoom Meeting",
            ),
        ),
    ]
