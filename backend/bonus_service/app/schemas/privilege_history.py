from datetime import datetime as dt
from uuid import UUID

from enums.status import PrivilegeHistoryStatus
from pydantic import BaseModel


class PrivilegeHistoryBase(BaseModel):
    privilege_id: int | None
    ticket_uid: UUID
    balance_diff: int
    operation_type: PrivilegeHistoryStatus


class PrivilegeHistoryFilter(BaseModel):
    privilege_id: int | None = None
    ticket_uid: UUID | None = None


class PrivilegeHistoryCreate(PrivilegeHistoryBase):
    privilege_id: int | None = None


class PrivilegeHistory(PrivilegeHistoryBase):
    id: int
    datetime: dt
