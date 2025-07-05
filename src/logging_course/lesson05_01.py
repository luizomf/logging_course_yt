# Essa é a função da aula 5:
# FileHandler e StreamHandler: usando nossos próprios Handlers com Logging - Aula 5
# https://youtu.be/z7LgK8KDcI0
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/

import logging
import sys

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Podemos criar nossos próprios handlers usando as classes que mencionei antes
file_handler = logging.FileHandler(
    filename="log.log",
    mode="a",
    encoding="utf-8",
)
stream_handler = logging.StreamHandler(sys.stdout)

# Nossos handlers precisam de um formatter
main_formatter = logging.Formatter(fmt=format1)

# A configuração do formatter pode ser reutilizada.
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)

# configura o root logger
logging.basicConfig(handlers=[file_handler, stream_handler])

# cria o meu logger
logger = logging.getLogger("meuapp")
# define o nível do meu log
logger.setLevel(logging.DEBUG)

# Saída nos dois handlers
logger.debug("mensagem de log")
logger.info("mensagem de log")
logger.warning("mensagem de log")
logger.error("mensagem de log")
logger.critical("mensagem de log")

# Exception
try:
    print(1 / 0)
except ZeroDivisionError:
    logger.exception("Alguém tentou dividir por zero aí.")
