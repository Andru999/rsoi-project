from typing import Annotated

from pydantic import BaseModel, constr


class AirportBase(BaseModel):
    name: Annotated[str, constr(max_length=255)] | None
    city: Annotated[str, constr(max_length=255)] | None
    country: Annotated[str, constr(max_length=255)] | None


class AirportCreate(AirportBase):
    name: Annotated[str, constr(max_length=255)] | None = None
    city: Annotated[str, constr(max_length=255)] | None = None
    country: Annotated[str, constr(max_length=255)] | None = None


class Airport(AirportBase):
    id: int
