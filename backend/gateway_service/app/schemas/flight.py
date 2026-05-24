from datetime import datetime as dt
from typing import Annotated

from pydantic import BaseModel, conint, constr


def convert_datetime(datetime: dt) -> str:
    return datetime.strftime("%Y-%m-%d %H:%M")


class FlightFilter(BaseModel):
    flightNumber: Annotated[str, constr(max_length=20)] | None = None
    minPrice: Annotated[int, conint(ge=1)] | None = None
    maxPrice: Annotated[int, conint(ge=1)] | None = None
    minDatetime: dt | None = None
    maxDatetime: dt | None = None


class FlightFilterGateway(FlightFilter):
    fromAirport: Annotated[str, constr(max_length=80)] | None = None
    toAirport: Annotated[str, constr(max_length=80)] | None = None


class FlightResponse(BaseModel):
    flightNumber: Annotated[str, constr(max_length=20)]
    fromAirport: str | None
    toAirport: str | None
    date: dt
    price: Annotated[int, conint(ge=1)]

    class Config:
        json_encoders = {
            dt: convert_datetime,
        }


class PaginationResponse(BaseModel):
    page: Annotated[int, conint(ge=1)]
    pageSize: Annotated[int, conint(ge=1)]
    totalElements: Annotated[int, conint(ge=0)]
    items: list[FlightResponse]
