import datetime

import pytz
import requests
import uvicorn
from exceptions.handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from routers.api import router as api_router
from utils.settings import get_settings

settings = get_settings()


def custom_openapi() -> dict:
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for method_item in app.openapi_schema.get("paths").values():
            for param in method_item.values():
                responses = param.get("responses")
                if "422" in responses:
                    del responses["422"]

        del app.openapi_schema["components"]["schemas"]["HTTPValidationError"]
        del app.openapi_schema["components"]["schemas"]["ValidationError"]

    return app.openapi_schema


app = FastAPI(
    title="Flight Booking System",
    version="v1",
)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")
app.openapi = custom_openapi


@app.middleware("http")
async def logs_handler(request: Request, call_next) -> Response:  # noqa: ANN001
    response: Response = await call_next(request)

    method = request.method
    url = request.url
    status_code = response.status_code
    current_time = datetime.datetime.now()
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = current_time.astimezone(moscow_timezone)

    data = f'{{"method": "{method}", "url": "{url}", "status_code": "{status_code}", "time": "{moscow_time}"}}'  # noqa: E501
    try:
        requests.post(
            url=f"http://{settings['services']['gateway']['statistics_host']}:"
            f"{settings['services']['statistics']['port']}/api/v1/statistics/produce",
            data=data,
        )
    except Exception as err:
        print(err)

    return response


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    return await request_validation_exception_handler(request, exc)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings["services"]["gateway"]["host"],
        port=settings["services"]["gateway"]["port"],
        log_level=settings["services"]["gateway"]["log_level"],
        reload=settings["services"]["gateway"]["reload"],
    )
