from collections.abc import Callable
from pathlib import Path
from typing import Literal

type LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
ALLOWED_LEVELS: set[LogLevel] = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def define_setting[T](value: T, validator: Callable[[T], T] | None = None) -> T:
    if validator is not None:
        return validator(value)
    return value


def validate_path_dir(path: Path) -> Path:
    if not path.is_dir():
        raise NotADirectoryError(path)
    return path


def validate_path_file(path: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def validate_level(level: str) -> LogLevel:
    if level not in ALLOWED_LEVELS:
        msg = f"Level {level!r} is not allowed. Use one of these: {ALLOWED_LEVELS}"
        raise ValueError(msg)
    return level


ROOT_DIR = define_setting(Path(".").resolve(), validator=validate_path_dir)
LOGS_DIR = define_setting(ROOT_DIR / "logs")
LOGGING_CONFIG_JSON = define_setting(
    ROOT_DIR / "logging.json", validator=validate_path_file
)

SETUP_LOGGER_NAME = define_setting("config_setup")
SETUP_LOGGER_LEVEL = define_setting("DEBUG", validator=validate_level)
