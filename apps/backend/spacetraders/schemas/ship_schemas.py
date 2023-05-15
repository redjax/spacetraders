from pydantic import BaseModel, validators, ValidationError, Field
from typing import Optional, Union, Any

from pathlib import Path


class SpaceTraderShipNavRouteCoord(BaseModel):
    symbol: str | None = None
    type: str | None = None
    systemSymbol: str | None = None
    x: int | None = None
    y: int | None = None


class SpaceTraderShipNavRoute(BaseModel):
    departure: SpaceTraderShipNavRouteCoord | None = None
    destination: SpaceTraderShipNavRouteCoord | None = None
    arrival: str | None = None
    departureTime: str | None = None


class SpaceTraderShipNav(BaseModel):
    systemSymbol: str | None = None
    waypointSymbol: str | None = None
    route: SpaceTraderShipNavRoute | None = None
    status: str | None = None
    flightMode: str | None = None


class SpaceTraderShipCrew(BaseModel):
    current: int | None = None
    capacity: int | None = None
    required: int | None = None
    rotation: str | None = None
    morale: int | None = None
    wages: int | None = None


class SpaceTraderShipFuelConsumed(BaseModel):
    amount: int | None = None
    timestamp: str | None = None


class SpaceTraderShipFuel(BaseModel):
    current: int | None = None
    capacity: int | None = None
    consumed: SpaceTraderShipFuelConsumed | None = None


class SpaceTraderShipFrameRequirements(BaseModel):
    power: int | None = None
    crew: int | None = None


class SpaceTraderShipFrame(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    moduleSlots: int | None = None
    mountingPoints: int | None = None
    fuelCapacity: int | None = None
    condition: int | None = None
    requirements: SpaceTraderShipFrameRequirements | None = None


class SpaceTraderShipReactorRequirements(BaseModel):
    crew: int | None = None


class SpaceTraderShipReactor(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    condition: int | None = None
    powerOutput: int | None = None
    requirements: SpaceTraderShipReactorRequirements | None = None


class SpaceTraderShipEngineRequirements(BaseModel):
    power: int | None = None
    crew: int | None = None


class SpaceTraderShipModuleRequirements(BaseModel):
    crew: int | None = None
    power: int | None = None
    slots: int | None = None


class SpaceTraderShipModule(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    capacity: int | None = None
    requirements: SpaceTraderShipModuleRequirements | None = None


class SpaceTraderShipEngine(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    condition: int | None = None
    speed: int | None = None
    requirements: SpaceTraderShipEngineRequirements | None = None


class SpaceTraderShipMountRequirements(BaseModel):
    crew: int | None = None
    power: int | None = None


class SpaceTraderShipMount(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    strength: int | None = None
    requirements: SpaceTraderShipMountRequirements | None = None
    deposits: list[str] | None = None


class SpaceTraderShipRegistration(BaseModel):
    name: str | None = None
    factionSymbol: str | None = None
    role: str | None = None


class SpaceTraderShipCargoInventoryItem(BaseModel):
    symbol: str | None = None
    name: str | None = None
    description: str | None = None
    units: int | None = None


class SpaceTraderShipCargo(BaseModel):
    capacity: int | None = None
    units: int | None = None
    inventory: list[SpaceTraderShipCargoInventoryItem] | None = None


class SpaceTraderShip(BaseModel):
    symbol: str | None = None
    nav: SpaceTraderShipNav | None = None
    crew: SpaceTraderShipCrew | None = None
    fuel: SpaceTraderShipFuel | None = None
    frame: SpaceTraderShipFrame | None = None
    reactor: SpaceTraderShipReactor | None = None
    engine: SpaceTraderShipEngine | None = None
    modules: list[SpaceTraderShipModule] | None = None
    mounts: list[SpaceTraderShipMount] | None = None
    registration: SpaceTraderShipRegistration | None = None
    cargo: SpaceTraderShipCargo | None = None
