import logging
import os
import sys

from typing import Optional

TRACE = 5

logging.addLevelName(TRACE, "TRACE")


DEFAULT_FORMAT = (
    "%(asctime)s %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] - %(message)s"
)

def get_level() -> str:
    """Get the default logging level for Basilisp."""
    return os.getenv("BASILISP_LOGGING_LEVEL", "ERROR")


def get_handler(
    level: Optional[str] = None, fmt: str = DEFAULT_FORMAT
) -> logging.Handler:
    """Get the default logging handler for Basilisp."""
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(fmt))
    handler.setLevel(level or get_level())
    return handler


def configure_root_logger(
    level: Optional[str] = None, fmt: str = DEFAULT_FORMAT
) -> None:
    """Configure the Basilisp root logger."""
    level = level or get_level()
    logger = logging.getLogger("basilisp")
    logger.setLevel(level)
    logger.addHandler(get_handler(level=level, fmt=fmt))
