from cruds.interfaces.privilege_history import IPrivilegeHistoryCRUD
from models.privilege_history import PrivilegeHistoryModel
from schemas.privilege_history import PrivilegeHistoryFilter
from sqlalchemy.orm import Query


class PrivilegeHistoryCRUD(IPrivilegeHistoryCRUD):
    async def get_all(
        self,
        privilege_history_filter: PrivilegeHistoryFilter,
    ) -> list[PrivilegeHistoryModel]:
        privilege_histories = self._db.query(PrivilegeHistoryModel)
        privilege_histories = await self.__filter_histories(
            privilege_histories,
            privilege_history_filter,
        )
        privilege_histories = privilege_histories.order_by(
            PrivilegeHistoryModel.id.desc(),
        )

        return privilege_histories.all()

    async def get_by_id(
        self,
        privilege_history_id: int,
    ) -> PrivilegeHistoryModel | None:
        return (
            self._db.query(PrivilegeHistoryModel)
            .filter(PrivilegeHistoryModel.id == privilege_history_id)
            .first()
        )

    async def add(
        self,
        privilege_history: PrivilegeHistoryModel,
    ) -> PrivilegeHistoryModel | None:
        try:
            self._db.add(privilege_history)
            self._db.commit()
            self._db.refresh(privilege_history)
        except:
            return None

        return privilege_history

    async def delete(
        self,
        privilege_history: PrivilegeHistoryModel,
    ) -> PrivilegeHistoryModel:
        self._db.delete(privilege_history)
        self._db.commit()

        return privilege_history

    async def __filter_histories(
        self,
        privilege_histories: Query,
        privilege_history_filter: PrivilegeHistoryFilter,
    ) -> Query:
        if privilege_history_filter.privilege_id:
            privilege_histories = privilege_histories.filter(
                PrivilegeHistoryModel.privilege_id
                == privilege_history_filter.privilege_id,
            )
        if privilege_history_filter.ticket_uid:
            privilege_histories = privilege_histories.filter(
                PrivilegeHistoryModel.ticket_uid
                == privilege_history_filter.ticket_uid,
            )

        return privilege_histories
