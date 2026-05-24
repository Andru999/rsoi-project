from typing import Annotated

from enums.status import PrivilegeStatus
from pydantic import BaseModel, conint, constr


class PrivilegeBase(BaseModel):
    username: Annotated[str, constr(max_length=80)]
    status: PrivilegeStatus
    balance: Annotated[int, conint(ge=0)] | None


class PrivilegeFilter(BaseModel):
    username: Annotated[str, constr(max_length=80)] | None = None
    status: PrivilegeStatus | None = None


class PrivilegeUpdate(BaseModel):
    status: PrivilegeStatus | None = None
    balance: Annotated[int, conint(ge=0)] | None = None


class PrivilegeCreate(PrivilegeBase):
    status: PrivilegeStatus = "BRONZE"
    balance: Annotated[int, conint(ge=0)] | None = None


class Privilege(PrivilegeBase):
    id: int
