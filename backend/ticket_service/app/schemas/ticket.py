from typing import Annotated
from uuid import UUID

from enums.status import TicketStatus
from pydantic import BaseModel, conint, constr


class TicketBase(BaseModel):
    username: Annotated[str, constr(max_length=80)]
    flight_number: Annotated[str, constr(max_length=20)]
    price: Annotated[int, conint(ge=0)]
    status: TicketStatus


class TicketFilter(BaseModel):
    username: Annotated[str, constr(max_length=80)] | None = None
    flight_number: Annotated[str, constr(max_length=20)] | None = None
    min_price: Annotated[int, conint(ge=0)] | None = None
    max_price: Annotated[int, conint(ge=0)] | None = None
    status: TicketStatus | None = None


class TicketUpdate(BaseModel):
    status: TicketStatus


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    ticket_uid: UUID
