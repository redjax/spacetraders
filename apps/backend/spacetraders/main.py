import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from pathlib import Path


from core.config import app_settings, api_settings, logging_settings
from util.constants import (
    default_req_cache_dir,
    default_serialize_dir,
    default_openapi_url,
    default_api_str,
    tags_metadata,
)
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

mkdirs = [default_serialize_dir, default_req_cache_dir]

for _p in mkdirs:
    if not Path(_p).exists():
        log.debug(f"Creating path: {_p}")
        Path(_p).mkdir(parents=True, exist_ok=True)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import api_router

from util.api import healthcheck

app = FastAPI(
    root_path="/",
    title=app_settings.APP_TITLE or "DEFAULT_TITLE",
    description=app_settings.APP_DESCRIPTION or "DEFAULT_DESCRIPTION",
    version=app_settings.APP_VERSION or "0.0.0",
    openapi_url=default_openapi_url,
    openapi_tags=tags_metadata,
)

## Include APIRouters
#  ex: app.include_router(some_route.router)
app.include_router(api_router.router)
app.include_router(healthcheck.router)

## Include sub-apps
#  ex: app.mount("/endpoint", app_name)

## Include other mounts

## Mount static dir, if exists
if Path("./static/").exists():
    print(f"[DEBUG] Path [static/] found. Mounting to app.")

    ## https://fastapi.tiangolo.com/tutorial/static-files/
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def hello_world() -> dict[str, str]:
    """Index page of root app."""
    return {"message": "Hello world."}
