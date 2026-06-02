import json

import requests
from cruds.base import BaseCRUD
from cruds.interfaces.flight import IFlightCRUD
from enums.sort import SortFlights
from fastapi import HTTPException, status
from requests import Response
from schemas.flight import FlightDatetimeUpdate, FlightFilter
from fastapi.security import HTTPAuthorizationCredentials
from utils.curcuit_breaker import CircuitBreaker
from utils.settings import get_settings
from utils.validate import validate_token_exists


class FlightCRUD(IFlightCRUD, BaseCRUD):
    def __init__(self, token: HTTPAuthorizationCredentials | None = None) -> None:
        settings = get_settings()
        flight_host = settings["services"]["gateway"]["flight_host"]
        flight_port = settings["services"]["flight"]["port"]

        self.http_path = f"http://{flight_host}:{flight_port}/api/v1/"
        self.token = token

    async def get_all_flights(
        self,
        flight_filter: FlightFilter,
        sort: SortFlights = SortFlights.IdAsc,
        page: int = 1,
        size: int = 100,
    ) -> dict:
        url = f"{self.http_path}flights/?page={page}&size={size}&sort={sort.value}"  # noqa: E501

        if flight_filter.flightNumber:
            url += f"&flight_number={flight_filter.flightNumber}"
        if flight_filter.minDatetime:
            url += f"&min_datetime={flight_filter.minDatetime}"
        if flight_filter.maxDatetime:
            url += f"&max_datetime={flight_filter.maxDatetime}"
        if flight_filter.minPrice:
            url += f"&min_price={flight_filter.minPrice}"
        if flight_filter.maxPrice:
            url += f"&max_price={flight_filter.maxPrice}"

        response: Response = CircuitBreaker.send_request(
            url=url,
            http_method=requests.get,
        )
        self._check_status_code(
            status_code=response.status_code,
            service_name="Flight Service",
        )

        return response.json()

    async def get_airport_by_id(self, airport_id: int) -> dict:
        response: Response = CircuitBreaker.send_request(
            url=f"{self.http_path}airports/{airport_id}/",
            http_method=requests.get,
        )
        self._check_status_code(
            status_code=response.status_code,
            service_name="Flight Service",
        )

        return response.json()

    async def update_flight_datetime_by_id(
        self,
        flight_id: int,
        flight_datetime_update: FlightDatetimeUpdate,
    ) -> dict:
        validate_token_exists(self.token)

        try:
            response: Response = requests.patch(
                url=f"{self.http_path}flights/{flight_id}/",
                data=json.dumps(
                    flight_datetime_update.model_dump(
                        mode="json",
                        exclude_unset=True,
                    ),
                ),
                headers={
                    "Authorization": self.token.scheme
                    + " "
                    + self.token.credentials,
                },
            )
        except:
            response = Response()
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

        if response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_404_NOT_FOUND,
        ]:
            detail = response.json().get("detail", "Invalid flight datetime")
            raise HTTPException(
                status_code=response.status_code,
                detail=detail,
            )

        self._check_status_code(
            status_code=response.status_code,
            service_name="Flight Service",
        )

        return response.json()
