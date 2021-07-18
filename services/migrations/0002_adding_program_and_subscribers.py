# -*- coding: utf-8 -*-
import utils.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0008_longer_slug"),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="program_html",
            field=utils.models.BleachRichTextField(blank=True, verbose_name="Program"),
        ),
        migrations.AddField(
            model_name="service",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                related_name="services",
                to="people.Person",
                verbose_name="Subscribers",
            ),
        ),
    ]
