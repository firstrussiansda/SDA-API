# -*- coding: utf-8 -*-
class RichTextMixin:
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

    TINYMCE_DEFAULT_CONFIG = {
        "selector": "textarea",
        "theme": "modern",
        "plugins": "link image code",
        "toolbar1": """
            undo redo |
            formatselect |
            bold italic underline |
            link |
            code
        """,
        "menubar": False,
        "inline": False,
        "statusbar": True,
        "width": "auto",
        "height": 360,
    }
