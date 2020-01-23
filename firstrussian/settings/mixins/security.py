# -*- coding: utf-8 -*-
class SecurityMixin:
    CSRF_COOKIE_HTTPONLY = False  # needed for django-csrf.js

    @property
    def CSRF_COOKIE_SECURE(self):
        return not self.DEVELOPMENT

    @property
    def SESSION_COOKIE_SECURE(self):
        return not self.DEVELOPMENT

    SECURE_HSTS_SECONDS = 31536000  # nginx
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False  # nginx
    SECURE_SSL_REDIRECT = False  # nginx
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    @property
    def AUTH_PASSWORD_VALIDATORS(self):
        return (
            [
                {
                    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
                },
                {
                    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
                    "OPTIONS": {"min_length": 10},
                },
                {
                    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
                },
                {
                    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
                },
            ]
            if not self.DEVELOPMENT
            else []
        )
