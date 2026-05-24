from sqlalchemy import Column, Integer, String
from utils.database import Base


class PrivilegeModel(Base):
    __tablename__ = "privilege"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), nullable=False, unique=True)
    status = Column(String(80), nullable=False, default="BRONZE")
    balance = Column(Integer)
