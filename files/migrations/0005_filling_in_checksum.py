# -*- coding: utf-8 -*-
import hashlib

from django.db import migrations


def generate_checksum(apps, schema_editor):
    Attachment = apps.get_model("files", "Attachment")
    for attachment in Attachment.objects.filter(checksum__exact=None):
        with attachment.file.open("rb") as fid:
            attachment.checksum = hashlib.sha256(fid.read()).hexdigest()
        attachment.save()


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0004_adding_file_checksum"),
    ]

    operations = [
        migrations.RunPython(generate_checksum),
    ]
