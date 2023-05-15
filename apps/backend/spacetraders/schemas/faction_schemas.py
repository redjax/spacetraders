from pydantic import BaseModel, validators, ValidationError, Field
from typing import Optional, Union, Any

from pathlib import Path


class SpaceTraderFactionTrait(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None


class SpaceTraderFaction(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    headquarters: str | None = None
    traits: list[SpaceTraderFactionTrait] | None = None
