from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, conint, validator


def convert_datetime_to_iso_8601(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


class StatisticsBase(BaseModel):
    method: str
    url: str
    status_code: str
    time: datetime

    class Config:
        json_encoders = {
            datetime: convert_datetime_to_iso_8601,
        }


class StatisticsCreate(BaseModel):
    method: str
    url: str
    status_code: str
    time: datetime

    @validator("time", pre=True)
    def datetime_validate(cls, dt):  # noqa: ANN001, ANN201, N805
        return datetime.fromisoformat(dt)


class StatisticsResponse(StatisticsBase):
    id: int


class StatisticsPaginationResponse(BaseModel):
    page: Annotated[int, conint(ge=1)]
    pageSize: Annotated[int, conint(ge=1)]
    totalElements: Annotated[int, conint(ge=0)]
    items: list[StatisticsResponse]
