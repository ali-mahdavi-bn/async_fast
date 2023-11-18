from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from backbone.configs import config

DEFAULT_URl = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DATABASE}"

DEFAULT_ENGIN = create_async_engine(DEFAULT_URl)

SessionLocal = async_sessionmaker(
    bind=DEFAULT_ENGIN,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionLocal()
    return db
