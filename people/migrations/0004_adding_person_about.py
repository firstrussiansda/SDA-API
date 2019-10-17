from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0003_position_translation")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="about",
            field=models.TextField(blank=True, verbose_name="About"),
        ),
        migrations.AddField(
            model_name="person",
            name="about_en",
            field=models.TextField(blank=True, null=True, verbose_name="About"),
        ),
        migrations.AddField(
            model_name="person",
            name="about_ru",
            field=models.TextField(blank=True, null=True, verbose_name="About"),
        ),
        migrations.AddField(
            model_name="person",
            name="about_uk",
            field=models.TextField(blank=True, null=True, verbose_name="About"),
        ),
    ]
