from django.utils import translation


class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET.get("lang"):
            try:
                language_code = translation.get_supported_language_variant(
                    request.GET["lang"]
                )
            except LookupError:
                pass
            else:
                if language_code != request.LANGUAGE_CODE:
                    translation.activate(language_code)
                    request.LANGUAGE_CODE = translation.get_language()

        return self.get_response(request)
