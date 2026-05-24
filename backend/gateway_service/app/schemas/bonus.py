from datetime import datetime as dt
from typing import Annotated
from uuid import UUID

from enums.status import PrivilegeHistoryStatus, PrivilegeStatus
from pydantic import BaseModel, conint, constr


def convert_datetime(datetime: dt) -> str:
    return datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


class PrivilegeShortInfo(BaseModel):
    balance: Annotated[int, conint(ge=0)]
    status: PrivilegeStatus


class BalanceHistory(BaseModel):
    date: dt
    ticketUid: UUID
    balanceDiff: int
    operationType: PrivilegeHistoryStatus

    class Config:
        json_encoders = {
            dt: convert_datetime,
        }


class PrivilegeInfoResponse(BaseModel):
    balance: Annotated[int, conint(ge=0)]
    status: PrivilegeStatus
    history: list[BalanceHistory]


class PrivilegeCreate(BaseModel):
    username: Annotated[str, constr(max_length=80)]
    status: PrivilegeStatus = "BRONZE"
    balance: Annotated[int, conint(ge=0)] | None = None


class PrivilegeUpdate(BaseModel):
    status: PrivilegeStatus | None = None
    balance: Annotated[int, conint(ge=0)] | None = None


class PrivilegeHistoryCreate(BaseModel):
    privilege_id: int | None
    ticket_uid: UUID
    balance_diff: int
    operation_type: PrivilegeHistoryStatus


class PrivilegeHistoryFilter(BaseModel):
    privilege_id: int | None = None
    ticket_uid: UUID | None = None
