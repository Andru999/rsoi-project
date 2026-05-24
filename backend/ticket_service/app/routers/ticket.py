from typing import Annotated
from uuid import UUID

from cruds.interfaces.ticket import ITicketCRUD
from cruds.ticket import TicketCRUD
from enums.auth import RoleEnum
from enums.responses import RespEnum
from enums.sort import SortTicket
from enums.status import TicketStatus
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from models.ticket import TicketModel
from schemas.ticket import Ticket, TicketCreate, TicketFilter, TicketUpdate
from services.ticket import TicketService
from sqlalchemy.orm import Session
from utils.auth_user import RoleChecker
from utils.database import get_db


def get_ticket_crud() -> type[ITicketCRUD]:
    return TicketCRUD


router = APIRouter(
    prefix="/tickets",
    tags=["Ticket REST API operations"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespEnum.InvalidData.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
    },
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[Ticket],
    responses={
        status.HTTP_200_OK: RespEnum.GetAll.value,
    },
)
async def get_all_tickets(
    db: Annotated[Session, Depends(get_db)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    username: Annotated[str | None, Query(max_length=80)] = None,
    flight_number: Annotated[str | None, Query(max_length=20)] = None,
    min_price: Annotated[int | None, Query(ge=1)] = None,
    max_price: Annotated[int | None, Query(ge=1)] = None,
    status: TicketStatus | None = None,
    sort_field: SortTicket = SortTicket.StatusDesc,
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 100,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> list[TicketModel]:
    return await TicketService(
        ticketCRUD=ticketCRUD,
        db=db,
    ).get_all(
        ticket_filter=TicketFilter(
            username=username,
            flight_number=flight_number,
            min_price=min_price,
            max_price=max_price,
            status=status,
        ),
        sort_field=sort_field,
        page=page,
        size=size,
    )


@router.get(
    "/{ticket_uid}/",
    status_code=status.HTTP_200_OK,
    response_model=Ticket,
    responses={
        status.HTTP_200_OK: RespEnum.GetByUID.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
    },
)
async def get_ticket_by_uid(
    db: Annotated[Session, Depends(get_db)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    ticket_uid: UUID,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> TicketModel:
    return await TicketService(
        ticketCRUD=ticketCRUD,
        db=db,
    ).get_by_uid(ticket_uid)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        status.HTTP_201_CREATED: RespEnum.Created.value,
    },
)
async def create_new_ticket(
    db: Annotated[Session, Depends(get_db)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    ticket_create: TicketCreate,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> Response:
    ticket = await TicketService(
        ticketCRUD=ticketCRUD,
        db=db,
    ).add(ticket_create)

    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"/api/v1/tickets/{ticket.ticket_uid}"},
    )


@router.delete(
    "/{ticket_uid}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespEnum.Delete.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
    },
)
async def remove_ticket_by_uid(
    db: Annotated[Session, Depends(get_db)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    ticket_uid: UUID,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> Response:
    await TicketService(
        ticketCRUD=ticketCRUD,
        db=db,
    ).delete(ticket_uid)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.patch(
    "/{ticket_uid}/",
    status_code=status.HTTP_200_OK,
    response_model=Ticket,
    responses={
        status.HTTP_200_OK: RespEnum.Patch.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
    },
)
async def update_ticket_by_uid(
    db: Annotated[Session, Depends(get_db)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    ticket_uid: UUID,
    ticket_update: TicketUpdate,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> TicketModel:
    return await TicketService(
        ticketCRUD=ticketCRUD,
        db=db,
    ).patch(ticket_uid, ticket_update)
