import json
import msgpack
from uuid import UUID, uuid4
from typing import Any, Optional, Union

from core.config import app_settings, api_settings, logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

from util.constants import (
    default_api_str,
    default_serialize_dir,
    default_req_cache_dir,
    tags_metadata,
    update_tags_metadata,
    register_url,
    base_headers,
)

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from util.request_utils import get_req_session
from util.validators import validate_username

session = get_req_session(session_name="spacetraders_testing", allowable_codes=[200])

router = APIRouter(
    prefix="/example", tags=["example"], responses={404: {"description": "Not found"}}
)


@router.get("/")
async def say_hello() -> dict[str, str]:
    return {"message": "Example root reached"}


@router.get("/register")
async def ex_register_rand_agent() -> JSONResponse:
    log.debug("Generating random agent ID.")
    agent_name = validate_username(username=str(uuid4()))
    log.debug(f"Agent name: {agent_name}")

    log.info("Opening request session")
    with session:
        ## must be 14 chars
        agent_name = validate_username(username=str(uuid4()))
        log.debug(f"Len agent_name: {len(agent_name)}")

        params = {"symbol": f"{agent_name}", "faction": "COSMIC"}

        log.debug(f"Requesting {register_url}, params: {params}")
        res = session.post(url=register_url, json=params, headers=base_headers)

        status_code = res.status_code
        cached = res.from_cache
        ok = res.ok
        reason = res.reason

        _json = res.json()

        if _json:
            try:
                with open(
                    f"{default_serialize_dir}/{agent_name}.msgpack", "wb"
                ) as outfile:
                    packed = msgpack.packb(_json)
                    outfile.write(packed)
            except Exception as exc:
                raise Exception(f"Unhandled exception writing msgpack. Detail: {exc}")

        log.debug(f"[{status_code}: {reason}] Response from {res.url}")
        log.debug(f"Response text type({type(res.text)}): {res.text}")

        if status_code in [200, 201]:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=_json)
        else:
            return JSONResponse(status_code=res.status_code, content=_json)


@router.get("register/{agent_name}")
async def ex_register_agent(agent_name: Optional[str] = None) -> JSONResponse:
    """Make request to Startrader API, register agent_name"""
    if not agent_name:
        log.debug("No agent name passed.")
        # agent_name = validate_username(username=str(uuid4()))
        return status.HTTP_400_BAD_REQUEST

    valid_user = validate_username(agent_name)

    if not valid_user:
        log.error(f"Invalid username: {agent_name}.")

        return status.HTTP_422_UNPROCESSABLE_ENTITY

    log.info("Opening request session")
    with session:
        ## must be 14 chars
        agent_name = validate_username(username=str(uuid4()))
        log.debug(f"Len agent_name: {len(agent_name)}")

        params = {"symbol": f"{agent_name}", "faction": "COSMIC"}

        log.debug(f"Requesting {register_url}, params: {params}")
        res = session.post(url=register_url, json=params, headers=base_headers)

        status_code = res.status_code
        cached = res.from_cache
        ok = res.ok
        reason = res.reason

        log.debug(f"[{res.url}] [{res.status_code}: {res.reason}]")
        log.debug(f"Results ({type(res)}): {res.text}")

        _json = res.json()

        if _json:
            try:
                with open(
                    f"{default_serialize_dir}/{agent_name}.msgpack", "wb"
                ) as outfile:
                    packed = msgpack.packb(_json)
                    outfile.write(packed)
            except Exception as exc:
                raise Exception(f"Unhandled exception writing msgpack. Detail: {exc}")

        log.debug(f"[{status_code}: {reason}] Response from {res.url}")
        log.debug(f"Response text type({type(res.text)}): {res.text}")

        if status_code in [200, 201]:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=_json)
        else:
            return JSONResponse(status_code=res.status_code, content=_json)
