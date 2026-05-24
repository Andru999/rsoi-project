from abc import ABC, abstractmethod
from uuid import UUID

from enums.sort import SortTicket
from models.ticket import TicketModel
from schemas.ticket import TicketFilter, TicketUpdate
from sqlalchemy.orm import Session


class ITicketCRUD(ABC):
    def __init__(self, db: Session) -> None:
        self._db = db

    @abstractmethod
    async def get_all(
        self,
        ticket_filter: TicketFilter,
        sort_field: SortTicket,
        offset: int = 0,
        limit: int = 100,
    ) -> list[TicketModel]:
        pass

    @abstractmethod
    async def get_by_uid(self, ticket_uid: UUID) -> TicketModel | None:
        pass

    @abstractmethod
    async def add(self, ticket: TicketModel) -> TicketModel | None:
        pass

    @abstractmethod
    async def delete(self, ticket: TicketModel) -> TicketModel:
        pass

    @abstractmethod
    async def patch(
        self,
        ticket: TicketModel,
        ticket_update: TicketUpdate,
    ) -> TicketModel | None:
        pass
