from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0002_adding_position")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="position_en",
            field=models.CharField(
                blank=True,
                help_text="Position in the church",
                max_length=128,
                null=True,
                verbose_name="Position",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="position_ru",
            field=models.CharField(
                blank=True,
                help_text="Position in the church",
                max_length=128,
                null=True,
                verbose_name="Position",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="position_uk",
            field=models.CharField(
                blank=True,
                help_text="Position in the church",
                max_length=128,
                null=True,
                verbose_name="Position",
            ),
        ),
    ]
