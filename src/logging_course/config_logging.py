import atexit
import json
import logging
from logging.config import dictConfig
from pathlib import Path
from typing import Any

ROOT_DIR = Path(".").resolve()
LOGS_DIR = ROOT_DIR / "logs"
LOGGING_CONFIG_JSON = ROOT_DIR / "logging.json"


def setup() -> None:
    if not LOGGING_CONFIG_JSON.is_file():
        msg = f"Logging config file does not exist: {LOGGING_CONFIG_JSON}"
        raise FileNotFoundError(msg)

    if not LOGS_DIR.is_dir():
        LOGS_DIR.mkdir(parents=True, exist_ok=True)

    with LOGGING_CONFIG_JSON.open("r", encoding="utf-8") as file:
        logging_config = json.load(file)

    dictConfig(logging_config)

    queue_handler = logging.getHandlerByName("queue")

    if queue_handler:
        queue_handler.listener.start()  # pyright: ignore
        atexit.register(stop_queue_listener)


def stop_queue_listener() -> None:
    queue_handler = logging.getHandlerByName("queue")
    queue_handler.listener.stop()  # pyright: ignore
    print("Queue listener stopped successfuly")


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf8") as file:
        lines = file.readlines()

    logs: list[dict[str, Any]] = []

    if not lines:
        return logs

    for line in lines:
        logs.append(json.loads(line))

    return logs


if __name__ == "__main__":
    from rich import print as p

    log_file = LOGS_DIR / "log.jsonl"

    for log in parse_jsonl(log_file):
        # This is just an example
        p(log)
