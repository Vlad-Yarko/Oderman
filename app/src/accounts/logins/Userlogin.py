from sqlalchemy import select
from app.src.databases.engine import main_session
from app.src.databases.models import User


class UserLogin:

    async def get_user(self, user_id):
        async with main_session() as session:
            user = await session.execute(select(User).where(User.id == user_id))
            self.__user = user.scalar()
        return self

    def create_user(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user.id)