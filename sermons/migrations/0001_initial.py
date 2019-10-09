import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("people", "0001_initial"), ("media", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Sermon",
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
                    "soundcloud_assets",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sermons",
                        to="media.SoundCloudAsset",
                        verbose_name="SoundCloud Assets",
                    ),
                ),
                (
                    "speakers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sermons",
                        to="people.Person",
                        verbose_name="Speakers",
                    ),
                ),
                (
                    "youtube_assets",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sermons",
                        to="media.YouTubeAsset",
                        verbose_name="YouTube Assets",
                    ),
                ),
            ],
            options={"verbose_name": "Sermon", "verbose_name_plural": "Sermons"},
        )
    ]
