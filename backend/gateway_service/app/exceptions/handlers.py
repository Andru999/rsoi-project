from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def http_exception_handler(
    request: Request,  # noqa: ARG001
    exc: HTTPException,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
        },
    )


async def request_validation_exception_handler(
    request: Request,  # noqa: ARG001
    exc: RequestValidationError,
) -> JSONResponse:
    errors = jsonable_encoder(exc.errors())
    errors_details = []

    for err in errors:
        details = {}
        details["type"] = err["type"]
        details["msg"] = err["msg"]
        details["loc"] = " -> ".join(map(str, err["loc"]))

        errors_details.append(details)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": "Invalid request",
            "errors": errors_details,
        },
    )
