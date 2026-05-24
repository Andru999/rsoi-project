from datetime import datetime as dt
from typing import Annotated
from uuid import UUID

from cruds.bonus import BonusCRUD
from cruds.flight import FlightCRUD
from cruds.interfaces.bonus import IBonusCRUD
from cruds.interfaces.flight import IFlightCRUD
from cruds.interfaces.ticket import ITicketCRUD
from cruds.ticket import TicketCRUD
from enums.auth import RoleEnum
from enums.responses import RespEnum
from enums.sort import SortFlights
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from fastapi.security import HTTPAuthorizationCredentials
from schemas.bonus import PrivilegeInfoResponse
from schemas.flight import FlightFilterGateway, PaginationResponse
from schemas.ticket import (
    TicketPurchaseRequest,
    TicketPurchaseResponse,
    TicketResponse,
)
from schemas.user import UserInfoResponse, UserPayloadDto
from services.gateway import GatewayService
from utils.auth_user import RoleChecker, get_current_user, http_bearer


def get_flight_crud() -> type[IFlightCRUD]:
    return FlightCRUD


def get_ticket_crud() -> type[ITicketCRUD]:
    return TicketCRUD


def get_bonus_crud() -> type[IBonusCRUD]:
    return BonusCRUD


router = APIRouter(
    tags=["Gateway API"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespEnum.InvalidData.value,
    },
)


@router.get(
    "/flights",
    status_code=status.HTTP_200_OK,
    response_model=PaginationResponse,
    responses={
        status.HTTP_200_OK: RespEnum.GetAllFlights.value,
    },
)
async def get_list_of_flights(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    flightNumber: Annotated[str | None, Query(max_length=20)] = None,
    minPrice: Annotated[int | None, Query(ge=1)] = None,
    maxPrice: Annotated[int | None, Query(ge=1)] = None,
    minDatetime: dt | None = None,
    maxDatetime: dt | None = None,
    fromAirport: Annotated[str | None, Query(max_length=80)] = None,
    toAirport: Annotated[str | None, Query(max_length=80)] = None,
    sort: SortFlights = SortFlights.IdAsc,
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 100,
) -> PaginationResponse:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
    ).get_list_of_flights(
        flight_filter=FlightFilterGateway(
            flightNumber=flightNumber,
            minPrice=minPrice,
            maxPrice=maxPrice,
            minDatetime=minDatetime,
            maxDatetime=maxDatetime,
            fromAirport=fromAirport,
            toAirport=toAirport,
        ),
        sort=sort,
        page=page,
        size=size,
    )


@router.get(
    "/tickets",
    status_code=status.HTTP_200_OK,
    response_model=list[TicketResponse],
    responses={
        status.HTTP_200_OK: RespEnum.GetAllTickets.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
    },
)
async def get_information_on_all_user_tickets(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> list[TicketResponse]:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).get_info_on_all_user_tickets(
        user_name=user.login,
    )


@router.get(
    "/tickets/{ticketUid}",
    status_code=status.HTTP_200_OK,
    response_model=TicketResponse,
    responses={
        status.HTTP_200_OK: RespEnum.GetTicket.value,
        status.HTTP_404_NOT_FOUND: RespEnum.TicketNotFound.value,
    },
)
async def get_information_on_user_ticket(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    ticketUid: UUID,
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> TicketResponse:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).get_info_on_user_ticket(
        user_name=user.login,
        ticket_uid=ticketUid,
    )


@router.post(
    "/tickets",
    status_code=status.HTTP_200_OK,
    response_model=TicketPurchaseResponse,
    responses={
        status.HTTP_200_OK: RespEnum.BuyTicket.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
        status.HTTP_404_NOT_FOUND: RespEnum.FlightNumberNotFound.value,
    },
)
async def buy_ticket(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    ticket_purchase_request: TicketPurchaseRequest,
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> TicketPurchaseResponse:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).buy_ticket(
        user_name=user.login,
        ticket_purchase_request=ticket_purchase_request,
    )


@router.delete(
    "/tickets/{ticketUid}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespEnum.TicketRefund.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
        status.HTTP_404_NOT_FOUND: RespEnum.TicketNotFound.value,
    },
)
async def ticket_refund(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    ticketUid: UUID,
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> Response:
    await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).ticket_refund(
        user_name=user.login,
        ticket_uid=ticketUid,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=UserInfoResponse,
    responses={
        status.HTTP_200_OK: RespEnum.GetMe.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
    },
)
async def get_user_information(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> UserInfoResponse:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).get_user_information(
        user_name=user.login,
    )


@router.get(
    "/privilege",
    status_code=status.HTTP_200_OK,
    response_model=PrivilegeInfoResponse,
    responses={
        status.HTTP_200_OK: RespEnum.GetPrivilege.value,
        status.HTTP_401_UNAUTHORIZED: RespEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespEnum.Forbidden.value,
    },
)
async def get_information_about_bonus_account(
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
    bonusCRUD: Annotated[IBonusCRUD, Depends(get_bonus_crud)],
    user: UserPayloadDto = Depends(get_current_user),
    token: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> PrivilegeInfoResponse:
    return await GatewayService(
        flightCRUD=flightCRUD,
        ticketCRUD=ticketCRUD,
        bonusCRUD=bonusCRUD,
        token=token,
    ).get_info_about_bonus_account(
        user_name=user.login,
    )
