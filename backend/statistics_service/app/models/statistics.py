from sqlalchemy import Column, DateTime, Integer, String
from utils.database import Base


class StatisticsModel(Base):
    __tablename__ = "statistics"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String)
    url = Column(String)
    status_code = Column(String)
    time = Column(DateTime(timezone=True), nullable=False)
