from abc import ABC, abstractmethod

from models.statistics import StatisticsModel
from sqlalchemy.orm import Session


class IStatisticsCRUD(ABC):
    def __init__(self, db: Session) -> None:
        self._db = db

    @abstractmethod
    async def get_all(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[StatisticsModel]:
        pass
