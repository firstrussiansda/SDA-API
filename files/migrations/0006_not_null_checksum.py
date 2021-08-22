# -*- coding: utf-8 -*-
import django_auxilium.models.fields.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0005_filling_in_checksum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="checksum",
            field=models.CharField(max_length=64, unique=True, verbose_name="Checksum"),
        ),
        migrations.AlterField(
            model_name="attachment",
            name="file",
            field=django_auxilium.models.fields.files.RandomFileField(
                help_text="Attachment file",
                upload_to="files/attachments",
                verbose_name="File",
            ),
        ),
    ]
