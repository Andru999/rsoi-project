from abc import ABC, abstractmethod

from enums.sort import SortFlights
from schemas.flight import FlightDatetimeUpdate, FlightFilter


class IFlightCRUD(ABC):
    @abstractmethod
    async def get_all_flights(
        self,
        flight_filter: FlightFilter,
        sort: SortFlights = SortFlights.IdAsc,
        page: int = 1,
        size: int = 100,
    ) -> list[dict]:
        pass

    @abstractmethod
    async def get_airport_by_id(
        self,
        airport_id: int,
    ) -> dict:
        pass

    @abstractmethod
    async def update_flight_datetime_by_id(
        self,
        flight_id: int,
        flight_datetime_update: FlightDatetimeUpdate,
    ) -> dict:
        pass
