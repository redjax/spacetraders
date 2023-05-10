from __future__ import annotations

from core.config import app_settings, logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

log.debug(f"App Settings: {app_settings}")

from datetime import timedelta
import json
import msgpack

from uuid import UUID, uuid4

from pydantic import create_model
from requests_cache import CachedHTTPResponse, CachedRequest, CachedResponse
from util.constants import (
    base_url,
    default_req_cache_dir,
    endpoint_register,
    register_url,
)
from util.request_utils import get_req_session

with open("example_response.json", "r+") as f:
    res = json.loads(f.read())

# log.debug(f"Test res ({type(res)}): {res}")

## Create an undefined Pydantic model from JSON
test = create_model("User", **res)

# log.debug(f"Test ({type(test)}): {test}")

# log.debug(f"Schema: {test.schema()}")

headers = {"Content-Type": "application/json"}

session = get_req_session(session_name="spacetraders_testing", allowable_codes=[200])
log.debug(f"Session: {session}")


def validate_username(username: str = None) -> bool:
    agent_name_limit: int = 14

    if not username:
        raise ValueError("Missing username value.")

    if not isinstance(username, str):
        raise ValueError("username must be a string.")

    if len(username) > agent_name_limit:
        username_trim = username[:14]

        return username_trim


with session:
    ## must be 14 chars
    agent_name = validate_username(username=str(uuid4()))
    log.debug(f"Len agent_name: {len(agent_name)}")

    params = {"symbol": f"{agent_name}", "faction": "COSMIC"}

    log.debug(f"Requesting {register_url}, params: {params}")
    res = session.post(url=register_url, json=params, headers=headers)

    status_code = res.status_code
    cached = res.from_cache
    ok = res.ok
    reason = res.reason

    # _json = res.json()

    log.debug(f"[{status_code}: {reason}] Response from {res.url}")
    log.debug(f"Response text: {res.text}")
