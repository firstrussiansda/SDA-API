# -*- coding: utf-8 -*-
class CKEditorMixin:
    # Which HTML tags are allowed
    BLEACH_ALLOWED_TAGS = [
        "p",
        "br",
        "b",
        "i",
        "u",
        "em",
        "strong",
        "a",
        "h1",
        "h2",
        "h3",
    ]

    # Which HTML attributes are allowed
    BLEACH_ALLOWED_ATTRIBUTES = ["href", "title", "style"]

    # Which CSS properties are allowed in 'style' attributes (assuming
    # style is an allowed attribute)
    BLEACH_ALLOWED_STYLES = [
        "font-family",
        "font-weight",
        "text-decoration",
        "font-variant",
    ]

    # Strip unknown tags if True, replace with HTML escaped characters if
    # False
    BLEACH_STRIP_TAGS = True

    # Strip comments, or leave them in.
    BLEACH_STRIP_COMMENTS = True

    BLEACH_DEFAULT_WIDGET = "ckeditor.widgets.CKEditorWidget"

    CKEDITOR_CONFIGS = {
        "default": {
            "removePlugins": "stylesheetparser",
            "allowedContent": " ".join(BLEACH_ALLOWED_TAGS + ["a[!href]"]),
        }
    }
