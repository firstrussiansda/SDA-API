# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_adding_attachments"),
        ("sermons", "0002_adding_sermon_series"),
    ]

    operations = [
        migrations.AddField(
            model_name="sermon",
            name="attachments",
            field=models.ManyToManyField(
                blank=True,
                related_name="sermons",
                to="files.Attachment",
                verbose_name="Attachments",
            ),
        ),
    ]
