from project.dao.models.user import User


class UserDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает всех пользователей"""
        return self.session.query(User).all()

    def get_one(self, username: str):
        """Возвращает пользователя по username"""
        return self.session.query(User).get(username)

    def create(self, data: dict):
        """Создаем нового пользователя"""
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update(self, data: dict):
        """Обновляем данные пользователя"""
        self.session.add(data)
        self.session.commit()

    def delete(self, username: str):
        """Удаляем пользователя по id"""
        user = self.get_one(username)
        self.session.delete(user)
        self.session.commit()