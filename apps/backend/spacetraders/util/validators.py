from __future__ import annotations

from typing import Union

from core.config import logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

valid_req_libs = ["requests", "requests-cache", "httpx"]


def validate_username(username: str = None) -> Union[bool, str]:
    agent_name_limit: int = 14

    if not username:
        raise ValueError("Missing username value.")

    if not isinstance(username, str):
        raise ValueError("username must be a string.")

    if len(username) > agent_name_limit:
        username_trim = username[:14]

        return username_trim

    return True
