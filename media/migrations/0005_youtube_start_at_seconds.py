# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0004_removing_default"),
    ]

    operations = [
        migrations.AddField(
            model_name="youtubeasset",
            name="start_at_seconds",
            field=models.IntegerField(
                blank=True,
                help_text="Start at time offset in seconds",
                null=True,
                verbose_name="Start At",
            ),
        ),
    ]
