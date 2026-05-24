from uuid import uuid4

from sqlalchemy import (
    UUID,
    CheckConstraint,
    Column,
    Integer,
    LargeBinary,
    String,
)
from utils.database import Base


class UserModel(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(
        UUID(as_uuid=True),
        default=uuid4,
        unique=True,
        nullable=False,
    )
    login = Column(String(255), unique=True, nullable=False)
    password = Column(LargeBinary(255), nullable=False)
    lastname = Column(String(255), unique=False, nullable=False)
    firstname = Column(String(255), unique=False, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(255), unique=True, nullable=False)
    role = Column(
        String(50),
        CheckConstraint("role IN ('USER', 'MODERATOR', 'ADMIN')"),
        default="USER",
        nullable=False,
    )
