from project.dao.user_dao import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        """Получает сессию"""
        self.dao = dao

    def get_all(self) -> list[dict]:
        """Возвращает всех пользователей"""
        return self.dao.get_all()

    def get_one(self, username: str):
        """Возвращает пользователя по username"""
        return self.dao.get_one(username)

    def create(self, data: dict):
        """Создаем нового пользователя"""
        self.dao.create(data)

    def update(self, data: dict, username: str):
        """Обновляем данные пользователя"""
        user = self.get_one(username) #todo переделать

        if "password" in data:
            user.password = data.get("password")

    def delete(self, username: str):
        """Удаляем пользователя по id"""
        self.dao.delete(username)
