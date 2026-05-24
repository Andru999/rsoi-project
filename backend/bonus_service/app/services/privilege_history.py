from cruds.interfaces.privilege_history import IPrivilegeHistoryCRUD
from exceptions.http_exceptions import ConflictException, NotFoundException
from models.privilege_history import PrivilegeHistoryModel
from schemas.privilege_history import (
    PrivilegeHistoryCreate,
    PrivilegeHistoryFilter,
)
from sqlalchemy.orm import Session


class PrivilegeHistoryService:
    def __init__(
        self,
        privilegeHistoryCRUD: type[IPrivilegeHistoryCRUD],
        db: Session,
    ) -> None:
        self._privilegeHistoryCRUD = privilegeHistoryCRUD(db)

    async def get_all(
        self,
        privilege_history_filter: PrivilegeHistoryFilter,
    ) -> list[PrivilegeHistoryModel]:
        return await self._privilegeHistoryCRUD.get_all(
            privilege_history_filter,
        )

    async def get_by_id(
        self,
        privilege_history_id: int,
    ) -> PrivilegeHistoryModel:
        privilege_history = await self._privilegeHistoryCRUD.get_by_id(
            privilege_history_id,
        )
        if privilege_history is None:
            raise NotFoundException(prefix="Get Privilege History")

        return privilege_history

    async def add(
        self,
        privilege_history_create: PrivilegeHistoryCreate,
    ) -> PrivilegeHistoryModel:
        privilege_history = PrivilegeHistoryModel(
            **privilege_history_create.model_dump(),
        )
        privilege_history = await self._privilegeHistoryCRUD.add(
            privilege_history,
        )
        if privilege_history is None:
            raise ConflictException(
                prefix="Add Privilege History",
                message="не существует привилегии с таким id",
            )

        return privilege_history

    async def delete(self, privilege_history_id: int) -> None:
        privilege_history = await self._privilegeHistoryCRUD.get_by_id(
            privilege_history_id,
        )
        if privilege_history is None:
            raise NotFoundException(prefix="Delete Privilege History")
