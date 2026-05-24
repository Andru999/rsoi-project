from models.airport import AirportModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from utils.database import Base


class FlightModel(Base):
    __tablename__ = "flight"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(20), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    datetime = Column(DateTime(timezone=True), nullable=False)
    from_airport_id = Column(Integer, ForeignKey(AirportModel.id))
    to_airport_id = Column(Integer, ForeignKey(AirportModel.id))
