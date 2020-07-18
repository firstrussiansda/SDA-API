# -*- coding: utf-8 -*-
from django.db import migrations
from django.utils.text import slugify


def fill_slug(apps, schema_editor) -> None:
    Person = apps.get_model("people", "Person")
    for person in Person.objects.all():
        person.slug = slugify(person.name_en or str(person.id))
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0005_adding_slug"),
    ]

    operations = [
        migrations.RunPython(fill_slug),
    ]
