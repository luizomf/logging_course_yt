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

import logging

from logging_course import config_logging

if __name__ == "__main__":
    config_logging.setup()

    logger = logging.getLogger("meuapp")

    logger.debug("mensagem de log")
    logger.info("mensagem de log")
    logger.warning("mensagem de log")
    logger.error("mensagem de log")
    logger.critical(
        "Meu nome é %s %s", "Luiz", "Otávio", extra={"contexto": "Qualquer coisa"}
    )
