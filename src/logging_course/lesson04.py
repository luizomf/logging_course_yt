# Essa é a função da aula 4:
# Entenda a hierarquia dos Loggers no Logging do Python - Aula 4
# https://youtu.be/62FE1GGoaR4
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/

import logging

# Formato do log - veja todos os atributos disponíveis em:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
format2 = "[ %(levelname)s ] %(message)s - %(filename)s:%(lineno)d"

################################################################################

# RootLogger
logging.basicConfig(level=logging.CRITICAL, format=format1)
root = logging.getLogger()

################################################################################

# meuapp Logger (filho do root por padrão)
logger = logging.getLogger("meuapp")
logger.setLevel(logging.ERROR)

################################################################################

# meuapp.child Logger (filho do meuapp pelo ponto no nome)
logger_child = logging.getLogger("meuapp.child")
logger_child.setLevel(logging.INFO)

print("Hierarquia de loggers")
print(f"Topo da árvore: {root.name}", "#", "Parent (pai):", root.parent)
print(f"logger {logger.name}", "#", "Parent (pai):", logger.parent)
print(f"Filho de logger {logger_child.name}", "#", "Parent (pai):", logger_child.parent)

# Saída:
# Hierarquia de loggers
# Topo da árvore: root          # Parent (pai): None
# logger meuapp                 # Parent (pai): <RootLogger root (CRITICAL)>
# Filho de logger: meuapp.child # Parent (pai): <Logger meuapp (ERROR)>
#
# Root -> meuapp -> meuapp.child
