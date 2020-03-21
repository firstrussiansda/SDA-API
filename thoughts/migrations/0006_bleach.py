# -*- coding: utf-8 -*-
import utils.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0005_unique_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thought",
            name="thought_html",
            field=utils.models.BleachRichTextField(),
        ),
        migrations.AlterField(
            model_name="thought",
            name="thought_html_en",
            field=utils.models.BleachRichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="thought",
            name="thought_html_ru",
            field=utils.models.BleachRichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="thought",
            name="thought_html_uk",
            field=utils.models.BleachRichTextField(null=True),
        ),
    ]
