from datetime import datetime as dt

from models.privilege import PrivilegeModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from utils.database import Base


class PrivilegeHistoryModel(Base):
    __tablename__ = "privilege_history"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    privilege_id = Column(Integer, ForeignKey(PrivilegeModel.id))
    ticket_uid = Column(UUID(as_uuid=True), nullable=False)
    datetime = Column(DateTime(), nullable=False, default=dt.utcnow)
    balance_diff = Column(Integer, nullable=False)
    operation_type = Column(String(20), nullable=False)
