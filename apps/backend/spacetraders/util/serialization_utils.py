from typing import Optional, Union
import msgpack
import json

from uuid import UUID, uuid4

from core.config import logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

from util.constants import default_serialize_dir

def msgpack_serialize(_json: dict = None, filename: str = None):
    if not _json:
        raise ValueError("Missing Python dict data to serialize")
    
    if not filename:
        log.debug(f"Missing filename. Generating a random filename.")
        
        filename = str(uuid4())
        
    if filename.endswith(".msgpack"):
        filename.replace(".msgpack", "")
        
    filename = f"{default_serialize_dir}/{filename}.msgpack"
        
    if _json:
        try:
            with open(
                f"{filename}.msgpack", "wb"
            ) as outfile:
                packed = msgpack.packb(_json)
                outfile.write(packed)
            
            return_obj = {"success": True, "detail": {"message": f"Data serialized to file {filename}"}}

        except Exception as exc:
            log.error({"exception": "Unhandled exception writing msgpack."}, exc_info=True)
            
            return_obj = {"success": False, "detail": {"message": f"{exc}"}}
            
    return return_obj
        