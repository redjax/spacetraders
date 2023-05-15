from pydantic import BaseModel, validators, ValidationError, Field
from typing import Optional, Union, Any

from pathlib import Path

from schemas import agent_schemas
from schemas import faction_schemas
from schemas import contract_schemas
from schemas import ship_schemas


class RegisterAgentResponse(BaseModel):
    token: str | None = None
    agent: agent_schemas.SpaceTraderAgent | None = None
    contract: contract_schemas.SpaceTraderContract | None = None
    faction: faction_schemas.SpaceTraderFaction | None = None
    ship: ship_schemas.SpaceTraderShip | None = None
