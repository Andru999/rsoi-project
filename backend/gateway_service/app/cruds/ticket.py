import json
from uuid import UUID

import requests
from cruds.base import BaseCRUD
from cruds.interfaces.ticket import ITicketCRUD
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from requests import Response
from schemas.ticket import TicketCreate, TicketUpdate
from utils.curcuit_breaker import CircuitBreaker
from utils.settings import get_settings
from utils.validate import validate_token_exists


class TicketCRUD(ITicketCRUD, BaseCRUD):
    def __init__(self, token: HTTPAuthorizationCredentials | None) -> None:
        settings = get_settings()
        ticket_host = settings["services"]["gateway"]["ticket_host"]
        ticket_port = settings["services"]["ticket"]["port"]

        self.http_path = f"http://{ticket_host}:{ticket_port}/api/v1/"
        self.token = token

    async def get_all_tickets(
        self,
        page: int = 1,
        size: int = 100,
        username: str | None = None,
    ) -> dict:
        validate_token_exists(self.token)

        response: Response = CircuitBreaker.send_request(
            url=f'{self.http_path}tickets/?page={page}&size={size}'
            f'{f"&username={username}" if username else ""}',
            http_method=requests.get,
            headers={
                "Authorization": self.token.scheme
                + " "
                + self.token.credentials,
            },
        )
        self._check_status_code(
            status_code=response.status_code,
            service_name="Ticket Service",
        )

        return response.json()

    async def get_ticket_by_uid(
        self,
        ticket_uid: UUID,
    ) -> dict:
        validate_token_exists(self.token)

        response: Response = CircuitBreaker.send_request(
            url=f"{self.http_path}tickets/{ticket_uid}/",
            http_method=requests.get,
            headers={
                "Authorization": self.token.scheme
                + " "
                + self.token.credentials,
            },
        )
        if response.status_code == status.HTTP_404_NOT_FOUND:
            return None

        self._check_status_code(
            status_code=response.status_code,
            service_name="Ticket Service",
        )

        return response.json()

    async def create_new_ticket(
        self,
        ticket_create: TicketCreate,
    ) -> str:
        validate_token_exists(self.token)

        try:
            response: Response = requests.post(
                url=f"{self.http_path}tickets/",
                data=json.dumps(
                    ticket_create.model_dump(mode="json", exclude_unset=True),
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

        self._check_status_code(
            status_code=response.status_code,
            service_name="Ticket Service",
        )

        location: str = response.headers["location"]
        return location.split("/")[-1]

    async def update_ticket(
        self,
        ticket_uid: UUID,
        ticket_update: TicketUpdate,
    ) -> dict:
        validate_token_exists(self.token)

        try:
            response: Response = requests.patch(
                url=f"{self.http_path}tickets/{ticket_uid}/",
                data=json.dumps(
                    ticket_update.model_dump(mode="json", exclude_unset=True),
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

        self._check_status_code(
            status_code=response.status_code,
            service_name="Ticket Service",
        )

        return response.json()

    async def delete_ticket(
        self,
        ticket_uid: UUID,
    ) -> None:
        validate_token_exists(self.token)

        try:
            response: Response = requests.delete(
                url=f"{self.http_path}tickets/{ticket_uid}/",
                headers={
                    "Authorization": self.token.scheme
                    + " "
                    + self.token.credentials,
                },
            )
        except:
            response = Response()
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

        self._check_status_code(
            status_code=response.status_code,
            service_name="Ticket Service",
        )
