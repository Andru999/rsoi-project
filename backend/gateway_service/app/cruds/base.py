import inspect

from exceptions.http_exceptions import (
    InvalidRequestException,
    ServiceUnavailableException,
)
from fastapi import status


class BaseCRUD:
    def _check_status_code(self, status_code: int, service_name: str) -> None:
        method = inspect.stack()[1][3]
        method = " ".join(method.split("_")).title()

        if status_code == status.HTTP_503_SERVICE_UNAVAILABLE:
            raise ServiceUnavailableException(
                message=f"{service_name} unavailable",
            )
        if status_code >= 400:  # noqa: PLR2004
            raise InvalidRequestException(
                prefix=method,
                status_code=status_code,
            )
