# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0002_adding_location_name")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image_url",
            field=models.URLField(
                help_text="You can find many free images at unsplash.com",
                max_length=512,
                verbose_name="Image URL",
            ),
        )
    ]
