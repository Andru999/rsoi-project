from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from utils.settings import get_db_url

engine = create_engine(
    url=get_db_url(),
    pool_size=30,
    max_overflow=20,
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


def get_session():  # noqa: ANN201
    for s in get_db():  # noqa: RET503
        return s


def create_tables() -> None:
    """Создание таблиц, если они еще не были созданы."""
    Base.metadata.create_all(bind=engine)
