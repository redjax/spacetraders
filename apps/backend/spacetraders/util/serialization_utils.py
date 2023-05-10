from typing import Optional, Union
import msgpack
import json
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

from pathlib import Path

from uuid import UUID, uuid4

from core.config import logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

from util.constants import default_serialize_dir
from util.validators import validate_serialization_filetype

def msgpack_serialize(_json: dict = None, filename: str = None) -> dict[str, Union[bool, dict[str, str]]]:
    if not _json:
        raise ValueError("Missing Python dict data to serialize")
    
    if not filename:
        log.debug(f"Missing filename. Generating a random filename.")
        
        filename = str(uuid4())
    
    if not validate_serialization_filetype(filename=filename):
        raise ValueError(f"Invalid filetype")
    
    if Path(filename).suffix:
        filename.replace(Path(filename).suffix, "")
    
        
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


def parquet_serialize(_json: dict = None, filename: str = None) -> dict:
    
    if not _json:
        raise ValueError("Missing Python dict data to serialize")
    
    if not filename:
        log.debug(f"Missing filename. Generating a random filename.")
        
        filename = str(uuid4())
        
    if not validate_serialization_filetype(filename=filename):
        raise ValueError(f"Invalid filetype")
        
    if Path(filename).suffix:
        filename.replace(Path(filename).suffix, "")
    
    df = pd.DataFrame(_json)
    
    data_table = pa.Table.from_pandas(df)
    
    filename = f"{default_serialize_dir}/{filename}.parquet"
    
    try:
        pq.write_table(data_table, filename)
        # with open(filename, "w+") as _out:
        #     pq.write_table(data_table, _out)
    except Exception as exc:
        raise Exception(f"Unhandled exception writing table to Parquet file. Exception detail: {exc}")