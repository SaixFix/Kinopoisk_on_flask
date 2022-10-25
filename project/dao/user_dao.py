from project.dao.base import BaseDAO
from project.models import User
from project.tools.security import generate_password_hash


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, login, password):
        try:
            self._db_session.add(User(email=login, password=generate_password_hash(password)))
            self._db_session.commit()

        except Exception as e:
            print(e)
            self._db_session.rollback()

    def get_user_by_login(self, login):

        try:
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == login).one()
            return stmt

        except Exception as e:
            print(e)
            return {}

    def update(self, login, data):

        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == login).update(data)
            self._db_session.commit()

        except Exception as e:
            print(e)
            self._db_session.rollback()