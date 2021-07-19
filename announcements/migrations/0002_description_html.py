# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="description",
            field=models.TextField(verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_en",
            field=models.TextField(verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_ru",
            field=models.TextField(verbose_name="Announcement"),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description_uk",
            field=models.TextField(verbose_name="Announcement"),
        ),
    ]
