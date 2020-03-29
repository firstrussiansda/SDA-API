# -*- coding: utf-8 -*-
import utils.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0003_bleach"),
    ]

    operations = [
        migrations.AddField(
            model_name="announcement",
            name="announcement_html",
            field=utils.models.BleachRichTextField(
                default="", verbose_name="Announcement"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="announcement",
            name="announcement_html_en",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
        migrations.AddField(
            model_name="announcement",
            name="announcement_html_ru",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
        migrations.AddField(
            model_name="announcement",
            name="announcement_html_uk",
            field=utils.models.BleachRichTextField(
                null=True, verbose_name="Announcement"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description",
            field=utils.models.BleachRichTextField(
                blank=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_en",
            field=utils.models.BleachRichTextField(
                blank=True, null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_ru",
            field=utils.models.BleachRichTextField(
                blank=True, null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_uk",
            field=utils.models.BleachRichTextField(
                blank=True, null=True, verbose_name="Description"
            ),
        ),
    ]
