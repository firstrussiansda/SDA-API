# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0008_longer_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="notifications_email",
            field=models.EmailField(
                blank=True,
                help_text="Email to receive notifications",
                max_length=254,
                verbose_name="Email",
            ),
        ),
    ]
