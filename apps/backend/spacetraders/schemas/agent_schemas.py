from pydantic import BaseModel, validators, ValidationError, Field
from typing import Optional, Union, Any

from pathlib import Path


class SpaceTraderAgent(BaseModel):
    accountId: str | None = None
    symbol: str | None = None
    headquarters: str | None = None
    credits: int | None = None
