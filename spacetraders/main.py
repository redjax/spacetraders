from __future__ import annotations

from core.config import app_settings, logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

log.debug(f"App Settings: {app_settings}")
