from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from utils.settings import get_db_url

engine = create_engine(
    url=get_db_url(),
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()


def get_db():  # noqa: ANN201
    """Получение сессии подключения к БД."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    """Создание таблиц, если они еще не были созданы."""
    Base.metadata.create_all(bind=engine)
