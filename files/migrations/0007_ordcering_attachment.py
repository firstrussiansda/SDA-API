# -*- coding: utf-8 -*-
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0006_not_null_checksum"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="attachment",
            options={
                "ordering": ["-created"],
                "verbose_name": "Attachment",
                "verbose_name_plural": "Attachments",
            },
        ),
    ]
