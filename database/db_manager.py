from sqlalchemy import select

from .engine import proceed_schemas, get_session_maker, create_async_engine
from .db_base import Base
from .User import User
from .Withdraw import Withdraw
from sqlalchemy.engine import URL
from data import config
from loader import session_maker_m, session_maker


async def start_db():
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=config.BD_USERNAME,
        password=config.DB_PASS,
        port=config.DB_PORT,
        host=config.HOST,
        database=config.DB_NAME)
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    session_maker_m[0] = session_maker
    async with session_maker() as session:
        await proceed_schemas(async_engine, Base)


async def get_user_by_uid(uid: int) -> User:
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            if user is not None:
                user = user[0]
            return user


async def set_last_captcha(uid: int, captcha: str) -> None:
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            if user is not None:
                user = user[0]
                user.last_captcha = captcha


async def set_user_work(uid: int, work: bool) -> None:
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            if user is not None:
                user = user[0]
                user.worked = work


async def set_user_wallet(uid: int, wallet: str) -> None:
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            if user is not None:
                user = user[0]
                user.wallet = wallet


async def change_user_balance(uid: int, val: float) -> None:
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            if user is not None:
                user = user[0]
                user.balance += val


async def add_user_in_db(uid: int):
    async with session_maker()() as session:
        async with session.begin():
            user = User(uid)
            await session.merge(user)


async def get_story_withdraw_by_uid(uid: int):
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(Withdraw).where(Withdraw.user_id == uid))
            withdraws: User = result.fetchall()
            return withdraws


async def add_story_withdraw(uid: int, money: int) -> None:
    async with session_maker()() as session:
        async with session.begin():
            withdraw = Withdraw(uid, money)
            await session.merge(withdraw)