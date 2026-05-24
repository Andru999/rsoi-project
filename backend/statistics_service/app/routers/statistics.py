from typing import Annotated

from confluent_kafka import Producer
from cruds.interfaces.statistics import IStatisticsCRUD
from cruds.statistics import StatisticsCRUD
from enums.auth import RoleEnum
from enums.response import ResponseClass
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from schemas.statistics import StatisticsCreate, StatisticsPaginationResponse
from services.statistics import StatisticsService
from sqlalchemy.orm import Session
from utils.auth_user import RoleChecker
from utils.database import get_db


def get_statistics_crud() -> type[IStatisticsCRUD]:
    return StatisticsCRUD


router = APIRouter(
    prefix="/statistics",
    tags=["Statistics API"],
    responses={
        status.HTTP_400_BAD_REQUEST: ResponseClass.InvalidData.value,
    },
)

producer_conf = {
    "bootstrap.servers": "kafka:29092",
    "client.id": "my-app",
}

producer = Producer(producer_conf)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=StatisticsPaginationResponse,
    responses={
        status.HTTP_200_OK: ResponseClass.GetAll.value,
        status.HTTP_401_UNAUTHORIZED: ResponseClass.NotAuthorized.value,
        status.HTTP_403_FORBIDDEN: ResponseClass.Forbidden.value,
    },
)
async def get_all(
    db: Annotated[Session, Depends(get_db)],
    statisticsCRUD: Annotated[IStatisticsCRUD, Depends(get_statistics_crud)],
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1)] = 100,
    _: bool = Depends(RoleChecker(allowed_roles=[RoleEnum.ADMIN])),
) -> StatisticsPaginationResponse:
    return await StatisticsService(
        statisticsCRUD=statisticsCRUD,
        db=db,
    ).get_all(
        page=page,
        size=size,
    )


@router.post(
    path="/produce",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
async def produce(
    statistics_produce: StatisticsCreate,
) -> Response:
    producer.produce(
        "my-topic",
        value=statistics_produce.model_dump_json().encode("utf-8"),
    )
    producer.flush()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
