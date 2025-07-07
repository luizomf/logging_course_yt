# Aula 8
# RotatingFileHandler e RichHandler no Logging do Python - Aula 8
# https://youtu.be/MQKBIt7C-e4
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#handlers-padrao-em-logginghandlers
import logging
from logging.config import dictConfig
from typing import Any

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
        "console": {"format": "%(message)s", "datefmt": "[%X]"},
    },
    "handlers": {
        "console": {
            "()": "rich.logging.RichHandler",
            "formatter": "console",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": False,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
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
    "root": {"handlers": ["console", "file"]},
    "loggers": {"meuapp": {"level": "DEBUG"}},
}
dictConfig(LOGGING_CONFIG)

# USO

logger = logging.getLogger("meuapp")


def dividir(x: float, y: float) -> float:
    logger.debug(
        "Recebi x=%.2f e y=%.2f", x, y, extra={"operation": f"{x = } / {y = }"}
    )  # isso é debug

    if y == 0:
        msg = f"Não posso dividir {x} por {y}"
        raise ZeroDivisionError(msg)  # E agora?

    resultado = x / y
    logger.info(
        "O resultado da conta x=%.2f / y=%.2f = %.2f",
        x,
        y,
        resultado,
        extra={"operation": f"{x} / {y} = {resultado}"},
    )
    return resultado


if __name__ == "__main__":
    dividir(10, 5)

    logger.debug("mensagem de log")
    logger.info("mensagem de log")
    logger.warning("mensagem de log")
    logger.error("mensagem de log")
    logger.critical("mensagem de log")

    try:
        dividir(10, 0)
    except ZeroDivisionError:
        logger.exception("Divisão por zero", stack_info=True)
