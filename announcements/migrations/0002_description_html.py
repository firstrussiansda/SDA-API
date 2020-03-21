# -*- coding: utf-8 -*-
import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="description",
            field=ckeditor.fields.RichTextField(verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_en",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_ru",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_uk",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Announcement"),
        ),
    ]
