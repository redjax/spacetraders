from __future__ import annotations

from typing import Union

from core.config import logging_settings, app_settings, api_settings
from util.logging.logger import get_logger

log = get_logger(__name__, level=logging_settings.LOG_LEVEL)

default_req_cache_dir = ".cache"

endpoint_register = "/register"

base_url = api_settings.BASE_URL

register_url = f"{base_url}{endpoint_register}"

# trefle_base_url = trefle_api_settings.BASE_URL
# token_str = trefle_api_settings.API_KEY

# all_genus_endpoint = "/genus"
# all_plants_endpoint = "/plants"
# all_species_endpoint = "/species"
