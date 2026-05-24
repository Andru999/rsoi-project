from uuid import UUID

from cruds.interfaces.ticket import ITicketCRUD
from enums.sort import SortTicket
from exceptions.http_exceptions import ConflictException, NotFoundException
from models.ticket import TicketModel
from schemas.ticket import TicketCreate, TicketFilter, TicketUpdate
from sqlalchemy.orm import Session
from typing_extensions import Self


class TicketService:
    def __init__(
        self: Self,
        ticketCRUD: type[ITicketCRUD],
        db: Session,
    ) -> None:
        self._ticketCRUD = ticketCRUD(db)

    async def get_all(
        self: Self,
        ticket_filter: TicketFilter,
        sort_field: SortTicket,
        page: int = 1,
        size: int = 100,
    ) -> list[TicketModel]:
        return await self._ticketCRUD.get_all(
            ticket_filter=ticket_filter,
            sort_field=sort_field,
            offset=(page - 1) * size,
            limit=size,
        )

    async def get_by_uid(self, ticket_uid: UUID) -> TicketModel:
        ticket = await self._ticketCRUD.get_by_uid(ticket_uid)
        if ticket is None:
            raise NotFoundException(prefix="Get Ticket")

        return ticket

    async def add(self, ticket_create: TicketCreate) -> TicketModel:
        ticket = TicketModel(**ticket_create.model_dump())
        ticket = await self._ticketCRUD.add(ticket)
        if ticket is None:
            raise ConflictException(prefix="Add Ticket")

        return ticket

    async def delete(self, ticket_uid: UUID) -> TicketModel:
        ticket = await self._ticketCRUD.get_by_uid(ticket_uid)
        if ticket is None:
            raise NotFoundException(prefix="Delete Ticket")

        return await self._ticketCRUD.delete(ticket)

    async def patch(
        self: Self,
        ticket_uid: UUID,
        ticket_update: TicketUpdate,
    ) -> TicketModel:
        ticket = await self._ticketCRUD.get_by_uid(ticket_uid)
        if ticket is None:
            raise NotFoundException(prefix="Update Ticket")

        ticket = await self._ticketCRUD.patch(ticket, ticket_update)
        if ticket is None:
            raise ConflictException(prefix="Update Ticket")

        return ticket
