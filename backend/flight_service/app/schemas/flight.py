from datetime import datetime as dt
from typing import Annotated

from pydantic import BaseModel, conint, constr


def convert_datetime_to_iso_8601_without_time_zone(datetime: dt) -> str:
    return datetime.strftime("%Y-%m-%d %H:%M")


class FlightBase(BaseModel):
    flight_number: Annotated[str, constr(max_length=20)]
    price: Annotated[int, conint(ge=1)]
    datetime: dt
    from_airport_id: Annotated[int, conint(ge=1)] | None
    to_airport_id: Annotated[int, conint(ge=1)] | None


class FlightFilter(BaseModel):
    flight_number: Annotated[str, constr(max_length=20)] | None = None
    min_price: Annotated[int, conint(ge=1)] | None = None
    max_price: Annotated[int, conint(ge=1)] | None = None
    min_datetime: dt | None = None
    max_datetime: dt | None = None


class FlightCreate(FlightBase):
    from_airport_id: Annotated[int, conint(ge=1)] | None = None
    to_airport_id: Annotated[int, conint(ge=1)] | None = None


class Flight(FlightBase):
    id: int

    class Config:
        json_encoders = {
            # custom output conversion for datetime
            dt: convert_datetime_to_iso_8601_without_time_zone,
        }
