# Essa é a função da aula 2:
# Entendendo os Componentes do Módulo Logging do Python - Aula 2
# https://youtu.be/JTjxLLq7OrI?si=NERd7EM5niXTBbg1
#
# Playlist:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI
#
# Artigo:
#
# https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/#conceitos-principais-loggers-handlers-formatters-e-filters
#
# Como desligo esse print em prod?
# Qual a gravidade do print? Foi correto? Foi erro?
# De onde veio essa mensagem? Cadê o contexto? Arquivo, módulo, linha, data?
# E se eu quiser salvar os erros em um arquivo, enviar por e-mail, Socket, etc?

# Log -> Um registro de determinado evento que ocorreu na aplicação (LogRecord)
# Logger -> É quem emite ou recebe os logs
# Handler -> Sabe para onde emitir os logs (console, e-mail, socket, http, etc)
# Formatter -> Sabe como formatar o log (texto, json, yaml, etc)
# Filter (Opcional) -> Pode fazer uma filtragem adicional nos logs

# Um logger tem um ou vários handlers
# Um handler tem um formatter
# Um handler tem um ou vários filters (opcional)

# Logger como receptor -> Tem Level e Filter
# Handler como receptor -> Tem Level e Filter

# LogRecord é o objeto do Log quando emitido -> Tem Level

# Emissor - Loggers
# Um Logger emite um LogRecord em um level (debug, info, warning, error, critical)

# Receptores - Loggers e Handlers (propagation True)
# Todos os loggers da aplicação recebem um LogRecord emitido
# Todos os Handlers dos Loggers recebem um LogRecord emitido

# Tanto Logger quanto Handler podem descartar um log
