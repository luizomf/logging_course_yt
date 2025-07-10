# Aula 11
# Como criar um Formatter JSON do zero para Python Logging - Aula 11
# https://youtu.be/jX4Ai-ZWkj4
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#criando-um-json-log-formatter

import json
import logging
from datetime import datetime
from typing import Any, override
from zoneinfo import ZoneInfo

# Constantes de Configuração
# Define o fuso horário para os logs, garantindo consistência independente do servidor.
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TZ_IDENTIFIER = "America/Sao_Paulo"
TZ = ZoneInfo(TZ_IDENTIFIER)

LOG_RECORD_KEYS = [
    "name",
    "msg",
    "args",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
    "taskName",
    "message",
]


class JSONLogFormatter(logging.Formatter):
    def __init__(
        self,
        include_keys: list[str] | None = None,
        datefmt: str = "%Y-%m-%dT%H:%M:%S%z",
    ) -> None:
        super().__init__()
        self.include_keys = (
            include_keys if include_keys is not None else LOG_RECORD_KEYS
        )
        self.datefmt = datefmt

    @override
    def format(self, record: logging.LogRecord) -> str:
        dict_record: dict[str, Any] = {
            key: getattr(record, key)
            for key in self.include_keys
            if key in LOG_RECORD_KEYS and getattr(record, key, None) is not None
        }

        if "created" in dict_record:
            # Sobrescrevi o método `formatTime` para retornar um datetime
            # ao invés de `struct_time` que é o padrão. Assim consigo trabalhar
            # com timezone.
            dict_record["created"] = self.formatTime(record, self.datefmt)

        if "message" in self.include_keys:
            dict_record["message"] = record.getMessage()

        if "exc_info" in dict_record and record.exc_info:
            # `exc_info` traz informações sobre exceções. Precisamos formatar
            # esse valor para uma string. Por sorte isso existe em `Formatter`.
            dict_record["exc_info"] = self.formatException(record.exc_info)

        if "stack_info" in dict_record and record.stack_info:
            # Aqui também precisamos formatar o valor do stack da exceção para str.
            dict_record["stack_info"] = self.formatStack(record.stack_info)

        # Caso utilize extras ao emitir o log
        # Ex.: logger.warning("Mensagem", extra={"contexto": "qualquer coisa"})
        # A chave "contexto" será adicionada ao log também
        for key, val in vars(record).items():
            if key in LOG_RECORD_KEYS:
                # Essas chaves nós tratamos antes
                continue

            if key not in self.include_keys:
                msg = f'Key {key!r} does not exist in "include_keys"'
                raise KeyError(msg)

            # Adicionamos a chave extra ao log
            dict_record[key] = val

        return json.dumps(dict_record, default=str)

    @override
    def formatTime(self, record: logging.LogRecord, datefmt: str | None = None) -> str:
        date = datetime.fromtimestamp(record.created, tz=TZ)

        if datefmt:
            return date.strftime(datefmt)

        return date.isoformat()
