# -*- coding: utf-8 -*-
from configurations import values


class EmailMixin:
    DEVELOPMENT: bool
    EMAIL_NOTIFICATIONS = values.Value()

    @property
    def EMAIL_BACKEND(self) -> str:
        if self.DEVELOPMENT:
            return "django.core.mail.backends.console.EmailBackend"
        else:
            return "anymail.backends.mailgun.EmailBackend"

    @property
    def ANYMAIL(self):
        return {
            "MAILGUN_API_KEY": values.Value(environ_name="MAILGUN_KEY"),
            "MAILGUN_SENDER_DOMAIN": values.Value(environ_name="MAILGUN_SERVER_NAME"),
        }
