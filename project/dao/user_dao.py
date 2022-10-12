from project.dao.models.user import User


class DirectorDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает всех пользователей"""
        return self.session.query(User).all()

    def get_one(self, did):
        """Возвращает пользователя по id"""
        return self.session.query(User).get(did)

    def create(self, data: dict):
        """Создаем нового пользователя"""
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update(self, data: dict):
        """Обновляем данные пользователя"""
        self.session.add(data)
        self.session.commit()

    def delete(self, did):
        """Удаляем пользователя по id"""
        user = self.get_one(did)
        self.session.delete(user)
        self.session.commit()