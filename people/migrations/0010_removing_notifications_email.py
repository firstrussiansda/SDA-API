# -*- coding: utf-8 -*-
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0009_adding_notifications_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="notifications_email",
        ),
    ]
