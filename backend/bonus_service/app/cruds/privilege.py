from cruds.interfaces.privilege import IPrivilegeCRUD
from models.privilege import PrivilegeModel
from schemas.privilege import PrivilegeFilter, PrivilegeUpdate
from sqlalchemy.orm import Query


class PrivilegeCRUD(IPrivilegeCRUD):
    async def get_all(
        self,
        privilege_filter: PrivilegeFilter,
        offset: int = 0,
        limit: int = 100,
    ) -> list[PrivilegeModel]:
        privileges = self._db.query(PrivilegeModel)
        privileges = await self.__filter_privileges(
            privileges,
            privilege_filter,
        )

        return privileges.offset(offset).limit(limit).all()

    async def get_by_id(self, privilege_id: int) -> PrivilegeModel | None:
        return (
            self._db.query(PrivilegeModel)
            .filter(PrivilegeModel.id == privilege_id)
            .first()
        )

    async def add(self, privilege: PrivilegeModel) -> PrivilegeModel | None:
        try:
            self._db.add(privilege)
            self._db.commit()
            self._db.refresh(privilege)
        except:
            return None

        return privilege

    async def delete(self, privilege: PrivilegeModel) -> PrivilegeModel:
        self._db.delete(privilege)
        self._db.commit()

        return privilege

    async def patch(
        self,
        privilege: PrivilegeModel,
        privilege_update: PrivilegeUpdate,
    ) -> PrivilegeModel | None:
        update_fields = privilege_update.model_dump(exclude_unset=True)
        for key, value in update_fields.items():
            setattr(privilege, key, value)

        try:
            self._db.add(privilege)
            self._db.commit()
            self._db.refresh(privilege)
        except:
            return None

        return privilege

    async def __filter_privileges(
        self,
        privileges: Query,
        privilege_filter: PrivilegeFilter,
    ) -> Query:
        if privilege_filter.username:
            privileges = privileges.filter(
                PrivilegeModel.username == privilege_filter.username,
            )
        if privilege_filter.status:
            privileges = privileges.filter(
                PrivilegeModel.status == privilege_filter.status.value,
            )

        return privileges
