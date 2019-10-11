from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("people", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="person",
            name="position",
            field=models.CharField(
                blank=True,
                help_text="Position in the church",
                max_length=128,
                verbose_name="Position",
            ),
        ),
    ]
