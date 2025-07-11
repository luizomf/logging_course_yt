import atexit
import json
import logging
from logging.config import dictConfig
from logging.handlers import QueueHandler, QueueListener
from pathlib import Path

SETUP_LOGGER_NAME = "config_logging" # Falta Corrigir (.env, privado)
SETUP_LOGGER_LEVEL = getattr(logging, "DEBUG", "DEBUG") # Falta Corrigir (.env, privado)

setup_logger = logging.getLogger(SETUP_LOGGER_NAME) # Falta Corrigir (privado)
setup_logger.setLevel(SETUP_LOGGER_LEVEL) # Falta Corrigir (privado)

ROOT_DIR = Path(".").resolve() # Tem outra alternativa (privado)
LOGS_DIR = ROOT_DIR / "logs"  # Falta corrigir (.env, privado)
LOGGING_CONFIG_JSON = ROOT_DIR / "logging.json"  # Falta Corrigir (.env, privado)

_setup_logging_done: bool = False
_default_queue_listener: QueueListener | None = None


def _setup_logging() -> None:
    global _default_queue_listener, _setup_logging_done

    if _setup_logging_done:
        setup_logger.debug("logging already configured, doing nothing for now")
        return

    if not LOGGING_CONFIG_JSON.is_file():
        msg = f"Logging config file does not exist: {LOGGING_CONFIG_JSON}"
        raise FileNotFoundError(msg)

    if not LOGS_DIR.is_dir():
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        setup_logger.debug("Logs directory created: %s", LOGS_DIR)

    with LOGGING_CONFIG_JSON.open("r", encoding="utf-8") as file:
        logging_config = json.load(file)
        setup_logger.debug("JSON config file loaded: %s", LOGGING_CONFIG_JSON)

    dictConfig(logging_config)

    queue_handlers = [
        handler
        for handler in logging.getLogger().handlers
        if isinstance(handler, QueueHandler)
    ]
    queue_handlers_count = len(queue_handlers)
    setup_logger.debug("QueueHandlers found: %d", queue_handlers_count)

    if queue_handlers_count > 1:
        msg = "Multiple QueueHandlers found in RootLogger, only one is supported"
        raise RuntimeError(msg)

    if queue_handlers:
        queue_handler = queue_handlers[0]
        setup_logger.debug("Found QueueHandler with name: '%s'", queue_handler.name)

        _default_queue_listener = queue_handler.listener

        if _default_queue_listener is not None:
            _default_queue_listener.start()
            atexit.register(_stop_queue_listener)

            setup_logger.debug(
                "QueueListener from QueueHandler '%s' started", queue_handler.name
            )
            setup_logger.debug(
                "Function '%s' registered with atexit", _stop_queue_listener.__name__
            )


    _setup_logging_done = True


def _stop_queue_listener() -> None:
    if _default_queue_listener is None:
        return

    _default_queue_listener.stop()
    # Falta corrigir - colocar antes de terminar o listener
    setup_logger.debug("Default listener will stop now, 👋 bye...")

# Tipagem

# Falta level
def get_logger(name: str = "") -> logging.Logger:
    if not _setup_logging_done:
        _setup_logging()

    logger = logging.getLogger(name)
    return logger
