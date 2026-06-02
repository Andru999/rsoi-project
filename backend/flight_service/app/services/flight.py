from datetime import datetime as dt

from cruds.interfaces.flight import IFlightCRUD
from enums.auth import BadRequestErrorTextEnum
from enums.sort import SortFlights
from exceptions.http_exceptions import (
    BadRequestException,
    ConflictException,
    NotFoundException,
)
from models.flight import FlightModel
from schemas.flight import FlightCreate, FlightFilter, FlightUpdate
from sqlalchemy.orm import Session


class FlightService:
    def __init__(self, flightCRUD: type[IFlightCRUD], db: Session) -> None:
        self._flightCRUD = flightCRUD(db)

    async def get_all(
        self,
        flight_filter: FlightFilter,
        sort: SortFlights,
        page: int = 1,
        size: int = 100,
    ) -> list[FlightModel]:
        return await self._flightCRUD.get_all(
            flight_filter=flight_filter,
            sort=sort,
            offset=(page - 1) * size,
            limit=size,
        )

    async def get_by_id(self, flight_id: int) -> FlightModel:
        flight = await self._flightCRUD.get_by_id(flight_id)
        if flight is None:
            raise NotFoundException(prefix="Get flight")

        return flight

    async def add(self, flight_create: FlightCreate) -> FlightModel:
        flight = FlightModel(**flight_create.model_dump())
        flight = await self._flightCRUD.add(flight)
        if flight is None:
            raise ConflictException(
                prefix="Add flight",
                message="либо flight_number уже занят, "
                "либо такого(их) аэропорта(ов) не существует",
            )

        return flight

    async def delete(self, flight_id: int) -> FlightModel:
        flight = await self._flightCRUD.get_by_id(flight_id)
        if flight is None:
            raise NotFoundException(prefix="Delete flight")

        return await self._flightCRUD.delete(flight)

    async def patch(
        self,
        flight_id: int,
        flight_update: FlightUpdate,
    ) -> FlightModel:
        flight = await self._flightCRUD.get_by_id(flight_id)
        if flight is None:
            raise NotFoundException(prefix="Update flight")

        self.__validate_future_datetime(flight_update.datetime)

        flight = await self._flightCRUD.patch(flight, flight_update)
        if flight is None:
            raise ConflictException(prefix="Update flight")

        return flight

    def __validate_future_datetime(self, new_datetime: dt) -> None:
        if new_datetime.tzinfo is not None and new_datetime.utcoffset() is not None:
            now = dt.now(tz=new_datetime.tzinfo)
        else:
            now = dt.now()

        if new_datetime <= now:
            raise BadRequestException(
                error_in=BadRequestErrorTextEnum.INVALID_PAYLOAD_FIELD,
                detail="время вылета должно быть в будущем",
            )
