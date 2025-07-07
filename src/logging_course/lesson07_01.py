# Essa é a função da aula 7:
# dictConfig - como usar um dicionário para configurar o Logging do Python - Aula 7
# https://youtu.be/d7YoH9r4sNo
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#dictconfig-agora-vamos-aos-negocios

# ruff: noqa: ERA001

# LOGGING_CONFIG: dict[str, Any] = {
#     "version": 1, # sempre o mesmo valor
#     "disable_existing_loggers": False, # para mim, sempre o mesmo valor
#     "formatters": {}, # aqui vem seus formatters
#     "handlers": {}, # aqui os handlers
#     "filters": {}, # aqui viriam os filters
#     "root": {}, # aqui as configurações do `root`
#     "loggers": {}, # aqui cada chave é um logger específico
# }

import logging
from logging.config import dictConfig
from typing import Any

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "root": {
            "class": "logging.Formatter",
            "format": "[ Dict ROOT:%(levelname)s ] %(message)s",
        },
        "file": {
            "class": "logging.Formatter",
            "format": (
                "Dict %(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
            ),
        },
        "stream": {
            "class": "logging.Formatter",
            "format": "Dict [ MEUAPP:%(levelname)s ] %(message)s",
        },
    },
    "handlers": {
        "root": {
            "class": "logging.StreamHandler",
            "formatter": "root",
            "stream": "ext://sys.stdout",
            "level": "WARNING",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "log.log",
            "mode": "w",
            "encoding": "utf8",
            "formatter": "file",
        },
        "stream": {
            "class": "logging.StreamHandler",
            "formatter": "stream",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {"handlers": ["root"]},
    "loggers": {"meuapp": {"level": "DEBUG", "handlers": ["file", "stream"]}},
}

dictConfig(LOGGING_CONFIG)

################################################################################

# USO
logger = logging.getLogger("meuapp")

logger.debug("mensagem de log")
logger.info("mensagem de log")
logger.warning("mensagem de log")
logger.error("mensagem de log")
logger.critical("mensagem de log")
