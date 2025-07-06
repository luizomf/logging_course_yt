# Essa é a função da aula 6:
# Handler e Formatter + addHandler + Propagation no Logging do Python - Aula 6
# https://youtu.be/7fCFueRe9jI
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#loggers-de-terceiros-podem-entrar-no-seu-log

# 1 - Como os logs de terceiros podem poluir seu log
# 2 - Como configurar o logger para sua lib
# 2 - Como configurar seu logger sem root logger
# 3 - Como desativar a propagação

import logging
import sys

from rich import print as rprint
from rich.markdown import Markdown

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Podemos criar nossos próprios handlers usando as classes que mencionei antes
file_handler = logging.FileHandler(
    filename="log.log",
    mode="w",
    encoding="utf-8",
)
stream_handler = logging.StreamHandler(sys.stdout)

# Nossos handlers precisam de um formatter
main_formatter = logging.Formatter(fmt=format1)

# A configuração do formatter pode ser reutilizada.
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)

# configura o root logger
stream_handler_root = logging.StreamHandler(sys.stdout)
stream_handler_root.setFormatter(
    logging.Formatter(fmt="ROOT: [ %(levelname)s ] %(message)s")
)
stream_handler_root.setLevel(logging.INFO)
logging.basicConfig(level=logging.WARNING, handlers=[stream_handler_root])

# cria o meu logger
logger = logging.getLogger("meuapp")
logger.propagate = True
# define o nível do meu log
logger.setLevel(logging.DEBUG)

# Adicionado handlers no meu logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Saída nos dois handlers
logger.info("mensagem de log")

# Renderiza Markdown
md = Markdown("# Nos Handlers de `A`\n\nEste é um `markdown`.")
rprint(md)
