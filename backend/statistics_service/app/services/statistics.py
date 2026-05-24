from cruds.interfaces.statistics import IStatisticsCRUD
from cruds.statistics import StatisticsCRUD
from models.statistics import StatisticsModel
from schemas.statistics import (
    StatisticsPaginationResponse,
    StatisticsResponse,
)
from sqlalchemy.orm import Session


class StatisticsService:
    def __init__(
        self,
        statisticsCRUD: type[IStatisticsCRUD],
        db: Session,
    ) -> None:
        self._statisticsCRUD: StatisticsCRUD = statisticsCRUD(db)

    async def get_all(
        self,
        page: int = 1,
        size: int = 100,
    ) -> StatisticsPaginationResponse:
        statistics: list[StatisticsModel]
        total_items: int
        statistics, total_items = await self._statisticsCRUD.get_all(
            offset=(page - 1) * size,
            limit=size,
        )

        statistics_items: list[StatisticsResponse] = []
        for statistic in statistics:
            statistics_items.append(
                StatisticsResponse(
                    id=statistic.id,
                    method=statistic.method,
                    url=statistic.url,
                    status_code=statistic.status_code,
                    time=statistic.time,
                ),
            )

        return StatisticsPaginationResponse(
            page=page,
            pageSize=size,
            totalElements=total_items,
            items=statistics_items,
        )
