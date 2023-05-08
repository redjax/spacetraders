from __future__ import annotations

from core.config import app_settings, logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

log.debug(f"App Settings: {app_settings}")

import json

from pydantic import create_model

with open("example_response.json", "r+") as f:
    res = json.loads(f.read())

# log.debug(f"Test res ({type(res)}): {res}")

## Create an undefined Pydantic model from JSON
test = create_model("User", **res)

# log.debug(f"Test ({type(test)}): {test}")

log.debug(f"Schema: {test.schema()}")
