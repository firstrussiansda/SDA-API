# -*- coding: utf-8 -*-
import multiprocessing
import typing

import structlog

from .django import DjangoMixin


def add_process_name(logger, method_name: str, event_dict: dict) -> dict:
    event_dict["process_name"] = multiprocessing.current_process().name
    return event_dict


class LoggingMixin(DjangoMixin):
    LOGGABLE_PACKAGES: typing.List[str] = []

    STRUCTLOG_SHARED_PROCESSORS = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        add_process_name,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
    ]
    STRUCTLOG_PROCESSORS = [
        structlog.processors.format_exc_info,
        structlog.processors.StackInfoRenderer(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ]

    def _setup_structlog(self) -> None:
        structlog.configure(
            processors=(
                [structlog.stdlib.filter_by_level]
                + self.STRUCTLOG_SHARED_PROCESSORS
                + self.STRUCTLOG_PROCESSORS
            ),
            context_class=structlog.threadlocal.wrap_dict(dict),
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

    def _get_loggable_packages(self) -> typing.List[str]:
        return self.LOGGABLE_PACKAGES + self.INSTALLED_APPS_PROJECT

    @property
    def LOGGING(self) -> typing.Dict[str, typing.Any]:
        self._setup_structlog()

        logging = {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "main": {
                    "()": structlog.stdlib.ProcessorFormatter,
                    "processor": (
                        structlog.processors.JSONRenderer()
                        if not self.DEVELOPMENT
                        else structlog.dev.ConsoleRenderer(colors=False)
                    ),
                    "foreign_pre_chain": self.STRUCTLOG_SHARED_PROCESSORS,
                }
            },
            "handlers": {
                "default": {
                    "level": "DEBUG" if self.DEBUG else "INFO",
                    "class": "logging.StreamHandler",
                    "formatter": "main",
                },
                "null": {"level": "INFO", "class": "logging.NullHandler"},
            },
            "loggers": {
                **{
                    k: {"level": "DEBUG", "handlers": ["default"]}
                    for k in self._get_loggable_packages()
                },
                **{
                    k: {"level": "INFO", "handlers": ["default"]}
                    for k in ["django.request", "celery", "werkzeug"]
                },
            },
        }

        return logging
