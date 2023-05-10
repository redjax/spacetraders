from __future__ import annotations

from typing import Union

from core.config import logging_settings
from util.logging.logger import get_logger

from pathlib import Path

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

valid_req_libs = ["requests", "requests-cache", "httpx"]
valid_serialization_filetypes = [".parquet", ".msgpack"]

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

def validate_serialization_filetype(filename: str = None) -> bool:
    """Validate a file's extension.
    
    Ensures a filename is valid for serialization. Split the filename into name and file ext,
    check the valid_serialization_filetypes list to ensure file extension is valid.
    """
    
    if not filename:
        raise ValueError("Missing filename to check")
    
    file_ext = Path(filename).suffix
    log.debug(f"File ext: {file_ext}")
    
    if not file_ext:
        return True
    
    if file_ext not in valid_serialization_filetypes:
        log.error({"message": ValueError(f"Invalid file extension: {file_ext}. Must be one of {valid_serialization_filetypes}")})
        return False
    
    return True