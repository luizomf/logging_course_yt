# Essa é a função da aula 5:
# FileHandler e StreamHandler: usando nossos próprios Handlers com Logging - Aula 5
# https://youtu.be/z7LgK8KDcI0
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#filehandler-saida-para-um-arquivo

import logging

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Migrar para arquivo: basta informar o caminho, modo de abertura e encoding.
logging.basicConfig(
    level=logging.DEBUG,
    format=format1,
    filename="log.log",
    filemode="a",
    encoding="utf-8",
)

# Meu logger -> meuapp (root -> meuapp)
logger = logging.getLogger("meuapp")

# Agora você não verá mais saída no console
logger.debug("Isso deve aparecer no arquivo log.log")
