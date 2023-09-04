from sqlalchemy import select

from database import User


async def get_current_money(session_maker, uid):
    async with session_maker()() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == uid))
            user: User = result.one_or_none()
            return user.balace