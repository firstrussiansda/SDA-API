from whitenoise.middleware import WhiteNoiseMiddleware

from django.conf import settings


class StaticAndMediaMiddleware(WhiteNoiseMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
