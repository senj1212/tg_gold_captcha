from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: URL | str) -> AsyncEngine:
    return _create_async_engine(url=url, echo=True, encoding="UTF-8", pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, Base) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False,)