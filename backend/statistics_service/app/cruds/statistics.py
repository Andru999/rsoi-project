from cruds.interfaces.statistics import IStatisticsCRUD
from models.statistics import StatisticsModel


class StatisticsCRUD(IStatisticsCRUD):
    async def get_all(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[list[StatisticsModel], int]:
        statistics = self._db.query(StatisticsModel)
        total = statistics.count()
        statistics = statistics.order_by(StatisticsModel.id.desc())

        return statistics.offset(offset).limit(limit).all(), total
