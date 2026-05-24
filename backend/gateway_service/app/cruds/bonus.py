import json

import requests
from cruds.base import BaseCRUD
from cruds.interfaces.bonus import IBonusCRUD
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from requests import Response
from schemas.bonus import (
    PrivilegeCreate,
    PrivilegeHistoryCreate,
    PrivilegeHistoryFilter,
    PrivilegeUpdate,
)
from utils.curcuit_breaker import CircuitBreaker
from utils.settings import get_settings
from utils.validate import validate_token_exists


class BonusCRUD(IBonusCRUD, BaseCRUD):
    def __init__(self, token: HTTPAuthorizationCredentials | None) -> None:
        settings = get_settings()
        bonus_host = settings["services"]["gateway"]["bonus_host"]
        bonus_port = settings["services"]["bonus"]["port"]

        self.http_path = f"http://{bonus_host}:{bonus_port}/api/v1/"
        self.token = token

    async def get_all_privileges(
        self,
        page: int = 1,
        size: int = 100,
        username: str | None = None,
    ) -> dict:
        validate_token_exists(self.token)

        response: Response = CircuitBreaker.send_request(
            url=f'{self.http_path}privileges/?page={page}&size={size}'
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
            service_name="Bonus Service",
        )

        return response.json()

    async def get_privilege_by_id(
        self,
        privilege_id: int,
    ) -> dict:
        validate_token_exists(self.token)

        response: Response = CircuitBreaker.send_request(
            url=f"{self.http_path}privileges/{privilege_id}/",
            http_method=requests.get,
            headers={
                "Authorization": self.token.scheme
                + " "
                + self.token.credentials,
            },
        )
        self._check_status_code(
            status_code=response.status_code,
            service_name="Bonus Service",
        )

        return response.json()

    async def create_new_privilege(
        self,
        privilege_create: PrivilegeCreate,
    ) -> int:
        validate_token_exists(self.token)

        try:
            response: Response = requests.post(
                url=f"{self.http_path}privileges/",
                data=json.dumps(privilege_create.model_dump()),
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
            service_name="Bonus Service",
        )

        location: str = response.headers["location"]
        return int(location.split("/")[-1])

    async def update_privilege_by_id(
        self,
        privilege_id: int,
        privilege_update: PrivilegeUpdate,
    ) -> dict:
        validate_token_exists(self.token)

        try:
            response: Response = requests.patch(
                url=f"{self.http_path}privileges/{privilege_id}/",
                data=json.dumps(
                    privilege_update.model_dump(
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

        self._check_status_code(
            status_code=response.status_code,
            service_name="Bonus Service",
        )

        return response.json()

    async def get_all_privilege_histories(
        self,
        ph_filter: PrivilegeHistoryFilter,
    ) -> dict:
        validate_token_exists(self.token)

        response: Response = CircuitBreaker.send_request(
            url=f'{self.http_path}privilege_histories/'
            f'{f"?privilege_id={ph_filter.privilege_id}&" if ph_filter.privilege_id else "?"}'  # noqa: E501
            f'{f"ticket_uid={ph_filter.ticket_uid}" if ph_filter.ticket_uid else ""}',  # noqa: E501
            http_method=requests.get,
            headers={
                "Authorization": self.token.scheme
                + " "
                + self.token.credentials,
            },
        )
        self._check_status_code(
            status_code=response.status_code,
            service_name="Bonus Service",
        )

        return response.json()

    async def create_new_privilege_history(
        self,
        privilege_history_create: PrivilegeHistoryCreate,
    ) -> int:
        validate_token_exists(self.token)

        try:
            response: Response = requests.post(
                url=f"{self.http_path}privilege_histories/",
                data=json.dumps(
                    privilege_history_create.model_dump(
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

        self._check_status_code(
            status_code=response.status_code,
            service_name="Bonus Service",
        )

        location: str = response.headers["location"]
        return int(location.split("/")[-1])
