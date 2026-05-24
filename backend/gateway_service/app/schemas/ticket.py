from datetime import datetime as dt
from typing import Annotated
from uuid import UUID

from enums.status import TicketStatus
from pydantic import BaseModel, conint, constr
from schemas.bonus import PrivilegeShortInfo


def convert_datetime(datetime: dt | str) -> str:
    try:
        res_datetime = datetime.strftime("%Y-%m-%d %H:%M")
    except:
        res_datetime = datetime

    return res_datetime


class TicketResponse(BaseModel):
    ticketUid: UUID
    flightNumber: Annotated[str, constr(max_length=20)]
    fromAirport: str | None
    toAirport: str | None
    date: dt | str
    price: Annotated[int, conint(ge=1)]
    status: TicketStatus

    class Config:
        json_encoders = {
            dt: convert_datetime,
        }


class TicketPurchaseRequest(BaseModel):
    flightNumber: Annotated[str, constr(max_length=20)]
    price: Annotated[int, conint(ge=1)]
    paidFromBalance: bool


class TicketPurchaseResponse(BaseModel):
    ticketUid: UUID
    flightNumber: Annotated[str, constr(max_length=20)]
    fromAirport: str | None
    toAirport: str | None
    date: dt | str
    price: Annotated[int, conint(ge=1)]
    paidByMoney: Annotated[int, conint(ge=0)]
    paidByBonuses: Annotated[int, conint(ge=0)]
    status: TicketStatus
    privilege: PrivilegeShortInfo

    class Config:
        json_encoders = {
            dt: convert_datetime,
        }


class TicketCreate(BaseModel):
    username: Annotated[str, constr(max_length=80)]
    flight_number: Annotated[str, constr(max_length=20)]
    price: Annotated[int, conint(ge=0)]
    status: TicketStatus


class TicketUpdate(BaseModel):
    status: TicketStatus
