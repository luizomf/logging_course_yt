# Aula 9
# Aprenda a criar Filter e Handler no Logging do Python - Aula 9
# https://youtu.be/v12r8hzeiv8
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#handlers-padrao-em-logginghandlers
import logging
import sys
from logging.config import dictConfig
from typing import Any

from rich.console import Console

console_stdout = Console(file=sys.stdout)
console_stderr = Console(file=sys.stderr)

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file": {
            "format": (
                "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
                "|%(funcName)s|%(module)s|%(process)d|%(processName)s|%(thread)d|%(threadName)s"
                "%(taskName)s"
            )
        },
        "console_stdout": {"format": "OUT: %(message)s", "datefmt": "[%X]"},
        "console_stderr": {"format": "ERR: %(message)s", "datefmt": "[%X]"},
    },
    "filters": {
        "max_level_info": {
            "()": "logging_course.filters.MaxLevelFilter",
            "max_level": "INFO",
        }
    },
    "handlers": {
        "console_stdout": {
            "()": "logging_course.handlers.MyRichHandler",
            "formatter": "console_stdout",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": False,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
            "file": "stdout",
            "level": "DEBUG",
            "filters": ["max_level_info"],
        },
        "console_stderr": {
            "()": "logging_course.handlers.MyRichHandler",
            "formatter": "console_stderr",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": False,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
            "file": "stderr",
            "level": "WARNING",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": "log.log",
            "maxBytes": 1024 * 1024 * 5,  # 5MiB 5242880
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    "root": {"handlers": ["console_stdout", "console_stderr", "file"]},
    "loggers": {"meuapp": {"level": "DEBUG"}},
}
dictConfig(LOGGING_CONFIG)

# USO

logger = logging.getLogger("meuapp")


if __name__ == "__main__":
    logger.debug("mensagem de log")
    logger.info("mensagem de log")
    logger.warning("mensagem de log")
    logger.error("mensagem de log")
    logger.critical("mensagem de log")
