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

import logging
import sys

################################################################################

# ROOT: Handlers e Formatter

# Formatters
root_format = "[ ROOT:%(levelname)s ] %(message)s"
root_formatter = logging.Formatter(fmt=root_format)

# Handlers
root_stream_handler = logging.StreamHandler(sys.stdout)
root_stream_handler.setFormatter(root_formatter)
root_stream_handler.setLevel(logging.WARNING)

# Root config
logging.basicConfig(handlers=[root_stream_handler])

################################################################################

# Meu logger (meuapp): Handlers e Formatters

# Formatters
file_format = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
stream_format = "[ MEUAPP:%(levelname)s ] %(message)s"

file_formatter = logging.Formatter(fmt=file_format)
stream_formatter = logging.Formatter(fmt=stream_format)

# Handlers
file_handler = logging.FileHandler(filename="log.log", mode="w", encoding="utf8")
stream_handler = logging.StreamHandler(sys.stdout)

file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

# Logger
logger = logging.getLogger("meuapp")
logger.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

################################################################################

# USO

logger.debug("mensagem de log")
logger.info("mensagem de log")
logger.warning("mensagem de log")
logger.error("mensagem de log")
logger.critical("mensagem de log")
