import atexit
import json
import logging
from logging.config import dictConfig
from logging.handlers import QueueHandler, QueueListener
from pathlib import Path

ROOT_DIR = Path(".").resolve()
LOGS_DIR = ROOT_DIR / "logs"
LOGGING_CONFIG_JSON = ROOT_DIR / "logging.json"

_setup_logging_done: bool = False
_default_queue_listener: QueueListener | None = None

_logger = logging.getLogger("config_setup")
_logger.setLevel("DEBUG")


def _setup_logging() -> None:
    global _setup_logging_done, _default_queue_listener

    if _setup_logging_done:
        _logger.debug("logging already configured, doing nothing for now")
        return

    if not LOGGING_CONFIG_JSON.is_file():
        msg = f"Logging config file does not exist: {LOGGING_CONFIG_JSON}"
        raise FileNotFoundError(msg)

    if not LOGS_DIR.is_dir():
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        _logger.debug("Logs directory created: %s", LOGS_DIR)

    with LOGGING_CONFIG_JSON.open("r", encoding="utf-8") as file:
        logging_config = json.load(file)
        _logger.debug("JSON config file loaded: %s", LOGGING_CONFIG_JSON)

    dictConfig(logging_config)

    queue_handlers = [
        handler
        for handler in logging.getLogger().handlers
        if isinstance(handler, QueueHandler)
    ]

    queue_handlers_count = len(queue_handlers)
    _logger.debug("QueueHandlers found: %d", queue_handlers_count)

    if queue_handlers_count > 1:
        msg = "This function does not allow more than one QueueHandler"
        raise RuntimeError(msg)

    if queue_handlers_count > 0:
        queue_handler = queue_handlers[0]
        _logger.debug("Found QueueHandler with name: '%s'", queue_handler.name)

        if queue_handler:
            _default_queue_listener = queue_handler.listener

            if _default_queue_listener is not None:
                _default_queue_listener.start()
                atexit.register(_stop_queue_listener)

                _logger.debug(
                    "QueueListener from QueueHandler '%s' started", queue_handler.name
                )

                _logger.debug(
                    "Function '%s' registered with atexit",
                    _stop_queue_listener.__name__,
                )

    _setup_logging_done = True


def _stop_queue_listener() -> None:
    if _default_queue_listener is None:
        return

    _logger.debug("Default listener will stop now, 👋 bye...")
    _default_queue_listener.stop()


def get_logger(name: str = "") -> logging.Logger:
    if not _setup_logging_done:
        _setup_logging()
        _logger.debug("'_setup_logging' used to configure Python logging.")

    return logging.getLogger(name)
