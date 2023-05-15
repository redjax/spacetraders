import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from pathlib import Path
from typing import Any

import random

from core.config import api_settings, app_settings, logging_settings
from util.constants import (
    default_api_str,
    default_openapi_url,
    default_req_cache_dir,
    default_serialize_dir,
    tags_metadata,
)
from util.logging.logger import get_logger
from util.serialization_utils import msgpack_deserialize, msgpack_serialize

from schemas.responses import agent_responses

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

serials_dir = Path(default_serialize_dir)

# log.debug(f"Serialize dir: {serials_dir}")

if not serials_dir.exists():
    raise FileNotFoundError(f"Serialization directory does not exist: {serials_dir}")

# log.info(f"Serialize dir exists: {serials_dir}")

_serial_files: list[Path] = []

for _f in serials_dir.glob("**/*"):
    # log.debug(f"_f: {_f}")
    if _f.is_file() and _f.suffix == ".msgpack":
        # log.debug(f"msgpack detected: {_f}")
        _serial_files.append(_f)

# log.debug(f"Found {len(_serial_files)} serialized files.")

rand_ind = random.randint(0, len(_serial_files) - 1)

# log.debug(f"Random index: {rand_ind}")
sample_file = _serial_files[rand_ind]

# log.info(f"Analyzing sample ({type(sample_file)}): {sample_file}")

sample_dict: dict[str, Any] = {
    "name": sample_file.name,
    "full_path": str(sample_file.resolve()),
    "stem": sample_file.stem,
    "suffix": sample_file.suffix,
    "anchor": sample_file.anchor,
    "parent": str(sample_file.parent),
    "deserialized": {},
}

# log.debug(f"Sample dict: {sample_dict}")


sample_deser = msgpack_deserialize(filename=sample_file)

# log.debug(f"Sample deserialized ({type(sample_deser)}): {sample_deser}")

sample_dict["deserialized"] = sample_deser

# log.debug(f"Sample dict: {sample_dict}")

sample_data = sample_deser["detail"]["unpacked"]["data"]
sample_keys = sample_data.keys()

_res = agent_responses.RegisterAgentResponse.parse_obj(sample_data)

# log.debug(f"Results ({type(_res)}): {_res}")

log.debug(f"Ship res: {_res.ship}")
