# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("services", "0003_removing_subscribers"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                related_name="services",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Subscribers",
            ),
        ),
    ]
