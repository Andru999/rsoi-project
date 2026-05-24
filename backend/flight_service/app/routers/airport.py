from typing import Annotated

from cruds.airport import AirportCRUD
from cruds.interfaces.airport import IAirportCRUD
from enums.auth import RoleEnum
from enums.responses import RespAirportEnum
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from models.airport import AirportModel
from schemas.airport import Airport, AirportCreate
from services.airport import AirportService
from sqlalchemy.orm import Session
from utils.auth_user import RoleChecker
from utils.database import get_db


def get_airport_crud() -> type[IAirportCRUD]:
    return AirportCRUD


router = APIRouter(
    prefix="/airports",
    tags=["Airport REST API operations"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespAirportEnum.InvalidData.value,
    },
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[Airport],
    responses={
        status.HTTP_200_OK: RespAirportEnum.GetAll.value,
    },
)
async def get_all_airports(
    db: Annotated[Session, Depends(get_db)],
    airportCRUD: Annotated[IAirportCRUD, Depends(get_airport_crud)],
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 100,
) -> list[AirportModel]:
    return await AirportService(
        airportCRUD=airportCRUD,
        db=db,
    ).get_all(
        page=page,
        size=size,
    )


@router.get(
    "/{airport_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Airport,
    responses={
        status.HTTP_200_OK: RespAirportEnum.GetByID.value,
        status.HTTP_404_NOT_FOUND: RespAirportEnum.NotFound.value,
    },
)
async def get_airport_by_id(
    db: Annotated[Session, Depends(get_db)],
    airportCRUD: Annotated[IAirportCRUD, Depends(get_airport_crud)],
    airport_id: int,
) -> AirportModel:
    return await AirportService(
        airportCRUD=airportCRUD,
        db=db,
    ).get_by_id(airport_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        status.HTTP_201_CREATED: RespAirportEnum.Created.value,
        status.HTTP_401_UNAUTHORIZED: RespAirportEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespAirportEnum.Forbidden.value,
    },
)
async def create_new_airport(
    db: Annotated[Session, Depends(get_db)],
    airportCRUD: Annotated[IAirportCRUD, Depends(get_airport_crud)],
    airport_create: AirportCreate,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.MODERATOR]),
    ),
) -> Response:
    airport = await AirportService(
        airportCRUD=airportCRUD,
        db=db,
    ).add(airport_create)

    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={"Location": f"/api/v1/airports/{airport.id}"},
    )


@router.delete(
    "/{airport_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespAirportEnum.Delete.value,
        status.HTTP_401_UNAUTHORIZED: RespAirportEnum.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: RespAirportEnum.Forbidden.value,
        status.HTTP_404_NOT_FOUND: RespAirportEnum.NotFound.value,
    },
)
async def remove_airport_by_id(
    db: Annotated[Session, Depends(get_db)],
    airportCRUD: Annotated[IAirportCRUD, Depends(get_airport_crud)],
    airport_id: int,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.MODERATOR]),
    ),
) -> Response:
    await AirportService(
        airportCRUD=airportCRUD,
        db=db,
    ).delete(airport_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
