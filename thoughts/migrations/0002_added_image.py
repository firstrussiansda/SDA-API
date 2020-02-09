# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="thought",
            name="image_description",
            field=models.CharField(
                blank=True, max_length=512, verbose_name="Image Description"
            ),
        ),
        migrations.AddField(
            model_name="thought",
            name="image_url",
            field=models.URLField(
                default="https://images.unsplash.com/photo-1515705576963-95cad62945b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
                help_text="You can find many free images at unsplash.com",
                max_length=512,
                verbose_name="Image URL",
            ),
            preserve_default=False,
        ),
    ]
