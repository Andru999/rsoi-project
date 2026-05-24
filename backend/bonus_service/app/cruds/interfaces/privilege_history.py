from abc import ABC, abstractmethod

from models.privilege_history import PrivilegeHistoryModel
from schemas.privilege_history import PrivilegeHistoryFilter
from sqlalchemy.orm import Session


class IPrivilegeHistoryCRUD(ABC):
    def __init__(self, db: Session) -> None:
        self._db = db

    @abstractmethod
    async def get_all(
        self,
        privilege_history_filter: PrivilegeHistoryFilter,
    ) -> list[PrivilegeHistoryModel]:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        privilege_history_id: int,
    ) -> PrivilegeHistoryModel | None:
        pass

    @abstractmethod
    async def add(
        self,
        privilege_history: PrivilegeHistoryModel,
    ) -> PrivilegeHistoryModel | None:
        pass

    @abstractmethod
    async def delete(
        self,
        privilege_history: PrivilegeHistoryModel,
    ) -> PrivilegeHistoryModel:
        pass
