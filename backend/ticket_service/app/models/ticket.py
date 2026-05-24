from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from utils.database import Base


class TicketModel(Base):
    __tablename__ = "ticket"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    ticket_uid = Column(
        UUID(as_uuid=True),
        default=uuid4,
        unique=True,
        nullable=False,
    )
    username = Column(String(80), nullable=False)
    flight_number = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
