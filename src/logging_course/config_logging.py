import json
from logging.config import dictConfig
from pathlib import Path

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
