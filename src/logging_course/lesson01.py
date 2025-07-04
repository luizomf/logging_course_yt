# Level
# log_record.level >= Logger config DEBUG    10
# log_record.level >= Logger config INFO     20
# log_record.level >= Logger config WARNING  30
# log_record.level >= Logger config ERROR    40
# log_record.level >= Logger config CRITICAL 50
import logging

# Receptor - configura um handler no root logger com nível DEBUG
logging.basicConfig(level=logging.DEBUG)  # Define o level mínimo como 10 DEBUG

# root logger (Emissor)
logging.debug("Olá log")  # emite um log level 10 (DEBUG)
logging.info("Olá log")  # emite um log level 20 (INFO)
logging.warning("Olá log")  # emite um log level 30 (WARNING)
logging.error("Olá log")  # emite um log level 40 (ERROR)
logging.critical("Olá log")  # emite um log level 50 (CRITICAL)

################################################################################
print("#" * 80, end="\n\n")

# Mesma coisa de usar logging
root = logging.getLogger()  # Obtém ou cria um logger (vazio = root)
print(f"{root = !r}")
print(f"{root.handlers = !r}")  # basicConfig criou um StreamHandler
print(f"{root.handlers[0].formatter = !r}")  # basicConfig configurou um Formatter

################################################################################
print("#" * 80, end="\n\n")

# Isso agora não faz nada porque o root logger já foi configurado
logging.basicConfig(level=logging.WARNING)
# Mas agora faz (⚠️ NÃO USE `force`)
logging.basicConfig(level=logging.WARNING, force=True)

# Mesma coisa de usar logging
root = logging.getLogger()  # Obtém ou cria um logger (vazio = root)

# root logger vindo de getLogger
root.debug("Olá log")
root.info("Olá log")
root.warning("Olá log")
root.error("Olá log")
root.critical("Olá log")

################################################################################
print("#" * 80, end="\n\n")

# Formato do log - veja todos os atributos disponíveis em:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
format2 = "[ %(levelname)s ] %(message)s - %(filename)s:%(lineno)d"

# Não é assim que usamos logging
# estou usando force apenas para modificar o logging enquanto explico
logging.basicConfig(level=logging.DEBUG, force=True, format=format1)

# root logger (emissor)
root.debug("Olá log")
root.info("Olá log")
root.warning("Olá log")
root.error("Olá log")
root.critical("Olá log")

################################################################################
print("#" * 80, end="\n\n")

# Nas libs, geralmente vamos usar o nosso próprio logger
logger = logging.getLogger("meuapp")  # cria ou obtém um logger chamado meuapp
logger.setLevel(logging.ERROR)  # Define o level (receptor) para seu logger

# Seu logger ainda não tem handlers ou formatters. Quando emitimos um log, ele
# será propagado pela cadeia de loggers até chegar ao root (padrão).
# Com propagação ativa, o log vai usar os handlers de todos os logger acima dele

# root logger
logger.debug("Olá log")
logger.info("Olá log")
logger.warning("Olá log")
logger.error("Olá log")
logger.critical("Olá log")


################################################################################
print("#" * 80, end="\n\n")


# Formato do log - veja todos os atributos disponíveis em:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
format2 = "[ %(levelname)s ] %(message)s - %(filename)s:%(lineno)d"

# Não é assim que usamos logging
# estou usando force apenas para modificar o logging enquanto explico
logging.basicConfig(level=logging.DEBUG, format=format1)

# Nas libs, geralmente vamos usar o nosso próprio logger
logger = logging.getLogger("meuapp")  # cria ou obtém um logger chamado meuapp
logger.setLevel(logging.DEBUG)  # Define o level (receptor) para seu logger
