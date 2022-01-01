# -*- coding: utf-8 -*-
from datetime import date, timedelta

from files.models import Attachment
from sermons.models import Sermon, SermonSeries


FIRST_DAY = date.today()
SERIES = "2022Q1"

series = SermonSeries.objects.get(title_en__startswith=SERIES)
attachments = Attachment.objects.filter(name_en__startswith=SERIES)

data = []

for i, (ru, en) in enumerate(data):
    sermon = Sermon(
        is_published=False,
        date=FIRST_DAY + timedelta(days=i * 7),
        series=series,
        title_ru=f"Урок {i + 1} {ru}",
        title_en=f"Lesson {i + 1} {en}",
    )
    sermon.clean()
    sermon.save()
    sermon.attachments.add(*attachments)
