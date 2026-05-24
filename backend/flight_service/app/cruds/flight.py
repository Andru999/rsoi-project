from cruds.interfaces.flight import IFlightCRUD
from enums.sort import SortFlights
from models.flight import FlightModel
from schemas.flight import FlightFilter
from sqlalchemy.orm import Query


class FlightCRUD(IFlightCRUD):
    async def get_all(
        self,
        flight_filter: FlightFilter,
        sort: SortFlights,
        offset: int = 0,
        limit: int = 100,
    ) -> list[FlightModel]:
        models = self._db.query(FlightModel)
        models = self.__filter_models(models, flight_filter)
        models = self.__sort_models(models, sort)

        return models.offset(offset).limit(limit).all()

    async def get_by_id(self, flight_id: int) -> FlightModel | None:
        return (
            self._db.query(FlightModel)
            .filter(FlightModel.id == flight_id)
            .first()
        )

    async def add(self, flight: FlightModel) -> FlightModel | None:
        try:
            self._db.add(flight)
            self._db.commit()
            self._db.refresh(flight)
        except:
            return None

        return flight

    async def delete(self, flight: FlightModel) -> FlightModel:
        self._db.delete(flight)
        self._db.commit()

        return flight

    def __filter_models(
        self,
        models: Query,
        flight_filter: FlightFilter,
    ) -> Query:
        if flight_filter.flight_number:
            models = models.filter(
                FlightModel.flight_number.like(
                    f"%{flight_filter.flight_number}%",
                ),
            )
        if flight_filter.min_price:
            models = models.filter(
                FlightModel.price >= flight_filter.min_price,
            )
        if flight_filter.max_price:
            models = models.filter(
                FlightModel.price <= flight_filter.max_price,
            )
        if flight_filter.min_datetime:
            models = models.filter(
                FlightModel.datetime >= flight_filter.min_datetime,
            )
        if flight_filter.max_datetime:
            models = models.filter(
                FlightModel.datetime <= flight_filter.max_datetime,
            )

        return models

    def __sort_models(
        self,
        models: Query,
        sort: SortFlights,
    ) -> Query:
        sort_args = {
            SortFlights.IdAsc: FlightModel.id,
            SortFlights.IdDesc: FlightModel.id.desc(),
            SortFlights.FlightNumberAsc: FlightModel.flight_number,
            SortFlights.FlightNumberDesc: FlightModel.flight_number.desc(),
            SortFlights.DateAsc: FlightModel.datetime,
            SortFlights.DateDesc: FlightModel.datetime.desc(),
            SortFlights.PriceAsc: FlightModel.price,
            SortFlights.PriceDesc: FlightModel.price.desc(),
        }

        return models.order_by(sort_args[sort])
