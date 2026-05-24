from datetime import datetime
from uuid import UUID

from enums.auth import RoleEnum
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from schemas.bonus import PrivilegeShortInfo
from schemas.ticket import TicketResponse


class UserInfoResponse(BaseModel):
    tickets: list[TicketResponse]
    privilege: PrivilegeShortInfo | dict[None, None]


class UserPayloadDto(BaseModel):
    sub: UUID
    login: str
    role: RoleEnum
    email: EmailStr | None = None
    phone: PhoneNumber | None = None
    lastname: str | None = None
    firstname: str | None = None
    type: str | None = None
    exp: datetime
    iat: datetime
