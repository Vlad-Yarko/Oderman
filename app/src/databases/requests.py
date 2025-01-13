from sqlalchemy import select, insert, update
from app.src.databases.engine import main_session
from app.src.databases.models import User, Pizza, Beverage


async def orm_find_account(user_name: str):
    async with main_session() as session:
        data = await session.execute(select(User).where(User.username == user_name))
        u = data.scalar()
    return u


async def orm_create_account(user_name: str, password: str):
    async with main_session() as session:
        await session.execute(insert(User)
                              .values(username=user_name,
                                      password=password))
        await session.commit()


async def orm_pizza_menu():
    async with main_session() as session:
        data = await session.execute(select(Pizza))
    return data.scalars()


async def orm_beverages_menu():
    async with main_session() as session:
        data = await session.execute(select(Beverage))
    return data.scalars()


async def orm_update_profile_image(username: str, image_path):
    async with main_session() as session:
        await session.execute(update(User).where(User.username == username).values(image_path=image_path))
        await session.commit()
