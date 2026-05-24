from cruds.interfaces.privilege import IPrivilegeCRUD
from exceptions.http_exceptions import ConflictException, NotFoundException
from models.privilege import PrivilegeModel
from schemas.privilege import PrivilegeCreate, PrivilegeFilter, PrivilegeUpdate
from sqlalchemy.orm import Session


class PrivilegeService:
    def __init__(
        self,
        privilegeCRUD: type[IPrivilegeCRUD],
        db: Session,
    ) -> None:
        self._privilegeCRUD = privilegeCRUD(db)

    async def get_all(
        self,
        privilege_filter: PrivilegeFilter,
        page: int = 1,
        size: int = 100,
    ) -> list[PrivilegeModel]:
        return await self._privilegeCRUD.get_all(
            privilege_filter=privilege_filter,
            offset=(page - 1) * size,
            limit=size,
        )

    async def get_by_id(self, privilege_id: int) -> PrivilegeModel:
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege is None:
            raise NotFoundException(prefix="Get Privilege")

        return privilege

    async def add(self, privilege_create: PrivilegeCreate) -> PrivilegeModel:
        privilege = PrivilegeModel(**privilege_create.model_dump())
        privilege = await self._privilegeCRUD.add(privilege)
        if privilege is None:
            raise ConflictException(prefix="Add Privilege")

        return privilege

    async def delete(self, privilege_id: int) -> PrivilegeModel:
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege is None:
            raise NotFoundException(prefix="Delete Privilege")

        return await self._privilegeCRUD.delete(privilege)

    async def patch(
        self,
        privilege_id: int,
        privilege_update: PrivilegeUpdate,
    ) -> PrivilegeModel:
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege is None:
            raise NotFoundException(prefix="Update Privilege")

        privilege = await self._privilegeCRUD.patch(
            privilege,
            privilege_update,
        )
        if privilege is None:
            raise ConflictException(prefix="Update Privilege")

        return privilege
