from uuid import UUID

from cruds.interfaces.ticket import ITicketCRUD
from enums.sort import SortTicket
from models.ticket import TicketModel
from schemas.ticket import TicketFilter, TicketUpdate
from sqlalchemy.orm import Query
from typing_extensions import Self


class TicketCRUD(ITicketCRUD):
    async def get_all(
        self: Self,
        ticket_filter: TicketFilter,
        sort_field: SortTicket,
        offset: int = 0,
        limit: int = 100,
    ) -> list[TicketModel]:
        tickets = self._db.query(TicketModel)
        tickets = await self.__filter_tickets(tickets, ticket_filter)
        tickets = await self.__sort_tickets(tickets, sort_field)

        return tickets.offset(offset).limit(limit).all()

    async def get_by_uid(self: Self, ticket_uid: UUID) -> TicketModel | None:
        return (
            self._db.query(TicketModel)
            .filter(TicketModel.ticket_uid == ticket_uid)
            .first()
        )

    async def add(self: Self, ticket: TicketModel) -> TicketModel | None:
        try:
            self._db.add(ticket)
            self._db.commit()
            self._db.refresh(ticket)
        except:
            return None

        return ticket

    async def delete(self: Self, ticket: TicketModel) -> TicketModel:
        self._db.delete(ticket)
        self._db.commit()

        return ticket

    async def patch(
        self: Self,
        ticket: TicketModel,
        ticket_update: TicketUpdate,
    ) -> TicketModel | None:
        update_fields = ticket_update.model_dump(exclude_unset=True)
        for key, value in update_fields.items():
            setattr(ticket, key, value)

        try:
            self._db.add(ticket)
            self._db.commit()
            self._db.refresh(ticket)
        except:
            return None

        return ticket

    async def __filter_tickets(
        self: Self,
        tickets: Query,
        ticket_filter: TicketFilter,
    ) -> Query:
        if ticket_filter.username:
            tickets = tickets.filter(
                TicketModel.username == ticket_filter.username,
            )

        if ticket_filter.flight_number:
            tickets = tickets.filter(
                TicketModel.flight_number == ticket_filter.flight_number,
            )

        if ticket_filter.min_price:
            tickets = tickets.filter(
                TicketModel.price >= ticket_filter.min_price,
            )

        if ticket_filter.max_price:
            tickets = tickets.filter(
                TicketModel.price <= ticket_filter.max_price,
            )

        if ticket_filter.status:
            tickets = tickets.filter(
                TicketModel.status == ticket_filter.status.value,
            )

        return tickets

    async def __sort_tickets(
        self: Self,
        tickets: Query,
        sort_field: SortTicket,
    ) -> Query:
        match sort_field:
            case SortTicket.UsernameAsc:
                tickets = tickets.order_by(
                    TicketModel.username,
                    TicketModel.id.desc(),
                )
            case SortTicket.UsernameDesc:
                tickets = tickets.order_by(
                    TicketModel.username.desc(),
                    TicketModel.id.desc(),
                )

            case SortTicket.FlightNumberAsc:
                tickets = tickets.order_by(
                    TicketModel.flight_number,
                    TicketModel.id.desc(),
                )
            case SortTicket.FlightNumberDesc:
                tickets = tickets.order_by(
                    TicketModel.flight_number.desc(),
                    TicketModel.id.desc(),
                )

            case SortTicket.PriceAsc:
                tickets = tickets.order_by(
                    TicketModel.price,
                    TicketModel.id.desc(),
                )
            case SortTicket.PriceDesc:
                tickets = tickets.order_by(
                    TicketModel.price.desc(),
                    TicketModel.id.desc(),
                )

            case SortTicket.StatusAsc:
                tickets = tickets.order_by(
                    TicketModel.status,
                    TicketModel.id.desc(),
                )
            case SortTicket.StatusDesc:
                tickets = tickets.order_by(
                    TicketModel.status.desc(),
                    TicketModel.id.desc(),
                )

            case SortTicket.IdDesc:
                tickets = tickets.order_by(TicketModel.id.desc())
            case _:
                tickets = tickets.order_by(TicketModel.id)

        return tickets
