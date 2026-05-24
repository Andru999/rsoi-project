from abc import ABC, abstractmethod

from fastapi.security import HTTPAuthorizationCredentials
from schemas.bonus import (
    PrivilegeCreate,
    PrivilegeHistoryCreate,
    PrivilegeHistoryFilter,
    PrivilegeUpdate,
)


class IBonusCRUD(ABC):
    def __init__(
        self,
        token: HTTPAuthorizationCredentials | None,
    ) -> None:
        self.token = token

    @abstractmethod
    async def get_all_privileges(
        self,
        page: int = 0,
        size: int = 100,
        username: str | None = None,
    ) -> list[dict]:
        pass

    @abstractmethod
    async def get_privilege_by_id(
        self,
        privilege_id: int,
    ) -> dict:
        pass

    @abstractmethod
    async def create_new_privilege(
        self,
        privilege_create: PrivilegeCreate,
    ) -> int:
        pass

    @abstractmethod
    async def update_privilege_by_id(
        self,
        privilege_id: int,
        privilege_update: PrivilegeUpdate,
    ) -> dict:
        pass

    @abstractmethod
    async def get_all_privilege_histories(
        self,
        ph_filter: PrivilegeHistoryFilter,
    ) -> list[dict]:
        pass

    @abstractmethod
    async def create_new_privilege_history(
        self,
        privilege_history_create: PrivilegeHistoryCreate,
    ) -> int:
        pass
