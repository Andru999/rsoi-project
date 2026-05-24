from datetime import datetime as dt
from typing import Annotated

from cruds.flight import FlightCRUD
from cruds.interfaces.flight import IFlightCRUD
from enums.auth import RoleEnum
from enums.responses import RespFlightEnum
from enums.sort import SortFlights
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from models.flight import FlightModel
from schemas.flight import Flight, FlightCreate, FlightFilter
from services.flight import FlightService
from sqlalchemy.orm import Session
from utils.auth_user import RoleChecker
from utils.database import get_db


def get_flight_crud() -> type[IFlightCRUD]:
    return FlightCRUD


router = APIRouter(
    prefix="/flights",
    tags=["Flight REST API operations"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespFlightEnum.InvalidData.value,
    },
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[Flight],
    responses={
        status.HTTP_200_OK: RespFlightEnum.GetAll.value,
    },
)
async def get_all_flights(
    db: Annotated[Session, Depends(get_db)],
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    flight_number: Annotated[str | None, Query(max_length=20)] = None,
    min_price: Annotated[int | None, Query(ge=1)] = None,
    max_price: Annotated[int | None, Query(ge=1)] = None,
    min_datetime: dt | None = None,
    max_datetime: dt | None = None,
    sort: SortFlights = SortFlights.IdAsc,
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 100,
) -> list[FlightModel]:
    return await FlightService(
        flightCRUD=flightCRUD,
        db=db,
    ).get_all(
        flight_filter=FlightFilter(
            flight_number=flight_number,
            min_price=min_price,
            max_price=max_price,
            min_datetime=min_datetime,
            max_datetime=max_datetime,
        ),
        sort=sort,
        page=page,
        size=size,
    )


@router.get(
    "/{flight_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Flight,
    responses={
        status.HTTP_200_OK: RespFlightEnum.GetByID.value,
        status.HTTP_404_NOT_FOUND: RespFlightEnum.NotFound.value,
    },
)
async def get_flight_by_id(
    db: Annotated[Session, Depends(get_db)],
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    flight_id: int,
) -> FlightModel:
    return await FlightService(
        flightCRUD=flightCRUD,
        db=db,
    ).get_by_id(flight_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        status.HTTP_201_CREATED: RespFlightEnum.Created.value,
        status.HTTP_401_UNAUTHORIZED: RespFlightEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespFlightEnum.Forbidden.value,
        status.HTTP_409_CONFLICT: RespFlightEnum.Conflict.value,
    },
)
async def create_new_flight(
    db: Annotated[Session, Depends(get_db)],
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    flight_create: FlightCreate,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.MODERATOR]),
    ),
) -> Response:
    flight = await FlightService(
        flightCRUD=flightCRUD,
        db=db,
    ).add(flight_create)

    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"/api/v1/flights/{flight.id}"},
    )


@router.delete(
    "/{flight_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespFlightEnum.Delete.value,
        status.HTTP_401_UNAUTHORIZED: RespFlightEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespFlightEnum.Forbidden.value,
        status.HTTP_404_NOT_FOUND: RespFlightEnum.NotFound.value,
    },
)
async def remove_flight_by_id(
    db: Annotated[Session, Depends(get_db)],
    flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
    flight_id: int,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.MODERATOR]),
    ),
) -> Response:
    await FlightService(
        flightCRUD=flightCRUD,
        db=db,
    ).delete(flight_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
