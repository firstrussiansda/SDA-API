# -*- coding: utf-8 -*-
import utils.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0002_description_html"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="description",
            field=utils.models.BleachRichTextField(verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_en",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_ru",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_uk",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
    ]
