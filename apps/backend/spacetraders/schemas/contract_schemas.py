from pydantic import BaseModel, validators, ValidationError, Field
from typing import Optional, Union, Any

from pathlib import Path


class SpaceTraderContractDeliverTerms(BaseModel):
    tradeSymbol: str | None = None
    destinationSymbol: str | None = None
    unitsRequired: int | None = None
    unitsFulfilled: int | None = None


class SpaceTraderContractTerms(BaseModel):
    deadline: str | None = None
    payment: dict[str, int] | None = None
    deliver: list[SpaceTraderContractDeliverTerms] | None = None
    accepted: bool | None = None
    fulfilled: bool | None = None
    expiration: str | None = None


class SpaceTraderContract(BaseModel):
    id: str | None = None
    factionSymbol: str | None = None
    type: str | None = None
    terms: SpaceTraderContractTerms | None = None
