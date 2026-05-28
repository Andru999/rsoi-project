import inspect
import requests
from fastapi import status
from requests import Response
from exceptions.http_exceptions import (
    InvalidRequestException,
    ServiceUnavailableException,
)

def __check_status_code(status_code: int, service_name: str) -> None:
    method = inspect.stack()[1][3]
    method = " ".join(method.split("_")).title()
    if status_code == status.HTTP_503_SERVICE_UNAVAILABLE:
        raise ServiceUnavailableException(message=f"{service_name} unavailable")
    if status_code >= 400:
        raise InvalidRequestException(prefix=method, status_code=status_code)

def get_request(url: str, params: str | None = None, timeout: float = 5.0) -> Response:
    try:
        response: Response = requests.get(url=url, params=params, timeout=timeout)
    except Exception:
        response = Response()
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    __check_status_code(response.status_code, "Auth Service")
    return response