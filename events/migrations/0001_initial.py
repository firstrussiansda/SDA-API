import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_uk",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_uk",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                ("date", models.DateField(null=True, verbose_name="Date")),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="Is Featured"),
                ),
                (
                    "image_url",
                    models.URLField(
                        blank=True, max_length=512, verbose_name="Image URL"
                    ),
                ),
                (
                    "image_description",
                    models.CharField(
                        blank=True, max_length=512, verbose_name="Image Description"
                    ),
                ),
            ],
            options={"verbose_name": "Event", "verbose_name_plural": "Events"},
        )
    ]
