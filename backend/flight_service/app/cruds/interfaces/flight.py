from abc import ABC, abstractmethod

from enums.sort import SortFlights
from models.flight import FlightModel
from schemas.flight import FlightFilter
from sqlalchemy.orm import Session


class IFlightCRUD(ABC):
    def __init__(self, db: Session) -> None:
        self._db = db

    @abstractmethod
    async def get_all(
        self,
        flight_filter: FlightFilter,
        sort: SortFlights,
        offset: int = 0,
        limit: int = 100,
    ) -> list[FlightModel]:
        pass

    @abstractmethod
    async def get_by_id(self, flight_id: int) -> FlightModel | None:
        pass

    @abstractmethod
    async def add(self, flight: FlightModel) -> FlightModel | None:
        pass

    @abstractmethod
    async def delete(self, flight: FlightModel) -> FlightModel:
        pass
