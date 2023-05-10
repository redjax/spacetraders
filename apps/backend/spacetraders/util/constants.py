from __future__ import annotations

from typing import Union

from core.config import api_settings, app_settings, logging_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

default_req_cache_dir = ".cache"
default_serialize_dir = ".serialize"

endpoint_register = "/register"

base_url = api_settings.BASE_URL

register_url = f"{base_url}{endpoint_register}"

base_headers = {"Content-Type": "application/json"}


## Add metadata to tags assigned throughout the app. If a router/endpoint's tags match
#  any of these, the description and other metadata will be applied on the docs page.
#  This tags_metadata can be imported and extended with tags_metadata.append(new_tags_dict).
#
#  You can also create a new list of tags ([{"name": ..., "description": ...}, ...]) and join
#  them with tags_metadata = tags_metadata + new_tags_list
tags_metadata = [
    {
        "name": "default",
        "description": "Tags have not been added to these endpoints/routers.",
    },
    {
        "name": "util",
        "description": "Utility functions, routes, & more. These utils are in the root of the app, and accessible by all sub-apps and routers.",
    },
]

## Route to openapi docs. This returns the docs site as a JSON object
#  If you set this to the same route as docs (i.e. /docs), you will only
#  get the openapi JSON response, no Swagger docs.
default_openapi_url = "/docs/openapi"

default_api_str = "/api/v1"


def update_tags_metadata(
    tags_metadata: list = tags_metadata,
    update_metadata: Union[list[dict[str, str]], dict[str, str]] = None,
):
    """Update the global tags_metadata list with new values.

    Import this function in another app, create a new list of tags (or
    a single tag dict, {"name": ..., "description": ...}), then pass both
    the imported tags_metadata and the new list/single instance of tag objects.

    This funciton will combine them into a new tags_metadata object
    """
    if not tags_metadata:
        raise ValueError("Missing value for tags_metadata")

    if not update_metadata:
        raise ValueError("Missing value for update_metadata")

    if isinstance(update_metadata, list):
        ## List of dicts was passed

        # print(f"[DEBUG] Detected list of new tags: {update_metadata}")

        tags_metadata = tags_metadata + update_metadata

        return_obj = tags_metadata

    elif isinstance(update_metadata, dict):
        ## Single tag dict was passed

        # print(f"[DEBUG] Detected single dict for new tag: {update_metadata}")

        tags_metadata.append(update_metadata)

        return_obj = tags_metadata

    else:
        raise ValueError(
            "Type of update_metadata must be one of list[dict[str,str]] or dict[str,str]"
        )

    return return_obj
