"""The root APIRouter object. Other routers are mounted to this one,
and this api_router.router is mounted in the main app, including all
sub-routers.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

## Import sub-routers
from routers.example import example_router
from util.constants import default_api_str, tags_metadata

router = APIRouter(responses={404: {"description": "Not found"}})

## Include any sub-routers here
#  ex: router.include_router(sub_router.router)
router.include_router(example_router.router)


# @router.get("/")
# async def api_router_index() -> dict[str, str]:
#     return {"message": "Root API router reached."}
