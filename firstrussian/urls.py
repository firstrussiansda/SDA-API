# -*- coding: utf-8 -*-
import events.urls
import files.urls
import media.urls
import people.urls
import rosetta.urls
import sermons.urls
import thoughts.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(title="FirstRussian API", default_version="v1"), public=True
)

urlpatterns = [
    # apis
    path("", include(events.urls.router.urls)),
    path("", include(sermons.urls.router.urls)),
    path("", include(people.urls.router.urls)),
    path("", include(media.urls.router.urls)),
    path("", include(files.urls.router.urls)),
    path("", include(thoughts.urls.router.urls)),
    path("", RedirectView.as_view(pattern_name="schema-swagger-ui"), name="api-root"),
    # api docs
    re_path(
        r"^swagger(?P<format>\.json)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # admin
    path("admin/", admin.site.urls),
    path("rosetta/", include(rosetta.urls.urlpatterns)),
]

if settings.DEVELOPMENT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
