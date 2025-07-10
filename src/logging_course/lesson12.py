# Aula 12
# QueueHandler e QueueListener: log sem travar sua aplicação - Aula 12
# https://youtu.be/jX4Ai-ZWkj4
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#queuehandler-queuelistener

import logging

from logging_course import config_logging

if __name__ == "__main__":
    config_logging.setup()

    x, y = 2, 3
    result = 2 + 3
    print(f"{x=}, {y=}, {result=}")

    logger = logging.getLogger("meuapp")

    logger.debug("mensagem de log")
    logger.info("mensagem de log")
    logger.warning("x=%s, y=%s, result=%s", x, y, result)
    logger.error("mensagem de log")
    logger.critical(
        "Meu nome é %s %s", "Luiz", "Otávio", extra={"contexto": "Qualquer coisa"}
    )

    print("Aqui vem meu código...")
