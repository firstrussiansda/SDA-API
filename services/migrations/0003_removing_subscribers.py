# -*- coding: utf-8 -*-
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_adding_program_and_subscribers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="subscribers",
        ),
    ]
