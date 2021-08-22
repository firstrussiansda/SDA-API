# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_adding_attachments"),
    ]

    operations = [
        migrations.AddField(
            model_name="attachment",
            name="checksum",
            field=models.CharField(
                editable=False,
                max_length=64,
                null=True,
                unique=True,
                verbose_name="Checksum",
            ),
        ),
    ]
